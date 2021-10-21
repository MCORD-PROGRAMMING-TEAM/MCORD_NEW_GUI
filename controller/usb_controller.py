from PySide6.QtCore import QThread, Signal
import serial.tools.list_ports
import time
import csv
from datetime import datetime, timedelta
import re

class USBController:
    def __init__(self,view,model) -> None:
        self._view = view
        self._model = model
        self.USB = None
        self.Add_ports_to_combobox()
        self.thread_udpdate_flag = False
        
        
    
    def Add_ports_to_combobox(self):
        import serial.tools.list_ports
        ports = serial.tools.list_ports.comports()
        available_ports_on =  [p.device for p in ports]
        
        self._view.ui.connection_combox.addItems(available_ports_on)
        self._view.ui.connection_combox.setCurrentIndex(-1)
        
    def set_current_device(self):
        comport = self._view.ui.connection_combox.currentText()
        self._model.comport = comport
        self._model.active_source = 'USB'
        
    def response_parser(self,text):
        print("PARSER ::: PARSER")
        if isinstance(text,list):
            text = [i.decode('utf-8').replace("\r\n","") for i in text]
            print(text)
            text = text[1:-1]
            self._view.update_console(f'OK: {text[0]}')
            return
        
        self._view.update_console(text)

    def create_usb_connect(self):
        self.USB = USBClinet(self._model.comport)
        self.USB.connect()
        self.response_parser('Connection has been open')
        
    def close_usb_connect(self,status):
        if self.USB:
            if not status:
                self.USB.quit()
        
    def usb_send_start(self,status):
        if status:
            self.usb_worker = USBThread(self.USB,'start',int(self._model.board_comlist[-1]))
            self.usb_worker.start()
            self.usb_worker.reponse.connect(self.response_parser)
            self.usb_worker.finished.connect(self.usb_worker.quit)
            
        else:
            
            self.usb_worker = USBThread(self.USB,'stop',self._model.current_board_number)
            self.usb_worker.start()
            self.usb_worker.reponse.connect(self.response_parser)
            self.usb_worker.finished.connect(self.usb_worker.quit)
            
    def usb_send_voltage(self):
        params = [self._model.active_board, self._model.active_master_voltage, self._model.active_slave_voltage]
        self.usb_worker = USBThread(self.USB,'set',params)
        self.usb_worker.start()
        self.usb_worker.reponse.connect(self.response_parser)
        self.usb_worker.finished.connect(self.usb_worker.quit)
        
        
        
    def usb_send_update(self):
        if self._model.thread_update_run_status:
            print("Not start another thread, one is running")
            return 
        
        self.usb_worker_update = USBThreadUpdate(self.USB,self._model)
        self.usb_worker_update.thread_status.connect(self.response_parser)
        self.usb_worker_update.thread_start.connect(self._model.get_thead_update_status)
        self.usb_worker_update.response.connect(self._view.update_params_table)
        self.usb_worker_update.finished.connect(self.test_end_thread)
        self.usb_worker_update.start()
        
    def usb_update_stop(self,status):
        if not status:
            if not self._model.valid_powerbuttons_status():
                self.usb_worker_update.easy_end_thread()
    
    def test_end_thread(self):
        print('Thread stopped')
        
    def test_buttons(self):
        checker = [button.isChecked() for button, _ in self._model.all_power_buttons.values()]
        print(checker)
       
        
        


class USBClinet:
    def __init__(self,COM_Port) -> None:
        self.COM_port = COM_Port
        self.boundrate = 115200
    
    def __del__(self):
        print("Connection has been closed")
        self.connection.close()
              
    def connect(self):
        self.connection = serial.Serial(self.COM_port,self.boundrate,timeout=1)
        self.connection_status = self.connection.isOpen()
        
        
        
    def send_command(self,command):
        if self.connection_status:
            try:
                self.connection.write(command)
                time.sleep(2)
                return self.connection.readlines()
            except Exception as e:
                print(e)
    def quit(self):
        print("Connection has been closed")
        self.connection.close()
     
        
class USBThread(QThread):
    reponse = Signal(list)
    
    def __init__(self, client, func, bn) -> None:
        super().__init__()
        self.client = client
        self.bn = bn
        self.func = func
 
    def run(self):
        if self.func == 'start':
            rdy_command = f'misc.init({self.bn})\r\n'
            res = self.client.send_command(rdy_command.encode())
            self.reponse.emit(res)
            rdy_command = f'misc.HVon({self.bn})\r\n'
            res = self.client.send_command(rdy_command.encode())
            self.reponse.emit(res)
            
        elif self.func == 'stop':
            rdy_command = f'misc.HVoff({self.bn})\r\n'
            res = self.client.send_command(rdy_command.encode())
            self.reponse.emit(res)
            
        elif self.func == 'set':
            rdy_command = f'afedrv.SetDac({int(self.bn[0])},{self.bn[1]},{self.bn[2]})\r\n'
            res = self.client.send_command(rdy_command.encode())
            self.reponse.emit(res)
            
        else:
            return 
        
        
class USBThreadUpdate(QThread):
    response = Signal(list)
    thread_status = Signal(str)
    thread_start = Signal(bool)
      
    def __init__(self,client,model):
        super().__init__()
        self.client = client
        self.model = model 
        self.run_status = True
        self.entire_wait_time = 30
        self.wait_time = 2
   
        
    def run(self):
        self.thread_start.emit(True)
        while self.run_status:
            
            print("Thread started and sleep")
            for i in range(self.entire_wait_time):
                    if self.run_status:
                        print(i)
                        self.sleep(self.wait_time)
                    else:
                        break
            print("Thread woke up")
             #to faster run thread
            if not self.run_status:
                break
            
            
            for board in self.model.board_comlist:
                command = f'afedrv.GetAdc({board},3)\r\n'
                v1 = self.client.send_command(command.encode())
                v1 = v1[1].decode()
                print(v1)
                command = f'afedrv.GetAdc({board},4)\r\n'
                v2 = self.client.send_command(command.encode())
                v2 = v2[1].decode()
                print(v2)
                command = f'afedrv.GetTemp({board})\r\n'
                temps = self.client.send_command(command.encode())
                temps = self.parser(temps)
                t1,t2 = list(map(int, re.findall(r'\d+', temps)))
                res = ["OK",(v1,t1),(v2,t2),board]
                self.response.emit(res)
                self.thread_status.emit("Update done")
            
            
        
                
    def parser(self,text):
        print("Thread ::: PARSER")
        if isinstance(text,list):
            text = [i.decode('utf-8').replace("\r\n","") for i in text]
            text = text[1:-1]
            return text[0]
    
    
    
    def easy_end_thread(self):
        self.thread_start.emit(False)
        self.run_status = False
            
        
    