from PySide6.QtCore import QThread, Signal
import time
import socket
import json



class LanController:
    def __init__(self,view,model) -> None:
        self._view = view 
        self._model = model
        self.LAN = None

    def allowed_only_lan(self):
        text = self._view.ui.connection_edit.text()
        result = self._model.valid_ipaddress(text)
        if result:
            self._model.ip = text
        self._view.change_if_ip_reponse(result)
    
    def set_current_device(self):
        self._model.active_source = 'LAN'
    
    def create_lan_client(self):
        self.LAN = LanClient()
        try:
            res = self.LAN.connect((self._model.ip,5555)).decode()
            self._view.update_console(res)
            self._model.connected_lan = True
        except:
            self._model.valid_ip = False
            self._model.connection_error()
    
   
        
    
    def close_lan_client(self):
        self.LAN.close_connection()
        
    
    def json_parser(self,obj):
        res = f'{obj[0]} : {obj[1:]}'
        self._view.update_console(res)
    

        
    def lan_send_start(self,status):
        if status:
            self.lan_worker = LanThread(self.LAN,'start',int(self._model.board_comlist[-1]))
            self.lan_worker.start()
            self.lan_worker.start_response.connect(self.json_parser)
            self.lan_worker.finished.connect(self.lan_worker.quit)
        else:
            self.lan_worker = LanThread(self.LAN,'stop',self._model.current_board_number)
            self.lan_worker.start()
            self.lan_worker.start_response.connect(self.json_parser)
            self.lan_worker.finished.connect(self.lan_worker.quit)
            
            
    def lan_send_voltage(self):
        mv,sv = self._model.simp_work_params[self._model.active_board][0],self._model.simp_work_params[self._model.active_board][1]
        params = [self._model.active_board, mv, sv]
        print(f'command : {params}')
        self.lan_worker = LanThread(self.LAN,'set',params)
        self.lan_worker.start()
        self.lan_worker.start_response.connect(self.json_parser)
        self.lan_worker.finished.connect(self.lan_worker.quit)
        
    def lan_send_update(self):
        if self._model.thread_update_run_status:
            print("Not start another thread, one is running")
            return
        
        self.lan_worker_update = LanThreadUpdate(self.LAN,self._model)
        self.lan_worker_update.response.connect(self.json_parser)
        self.lan_worker_update.response.connect(self._view.update_params_table)
        self.lan_worker_update.thread_start.connect(self._model.get_thead_update_status)
        self.lan_worker_update.finished.connect(self.test_end_thread)
        self.lan_worker_update.start()
       
    def lan_update_stop(self,status):
        if not status:
            if not self._model.valid_powerbuttons_status():
                self.lan_worker_update.easy_end_thread()
    
    def test_end_thread(self):
        print('Thread stopped')
           
    

        

class LanClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      
  
    def connect(self,args):
            try:
                self.sock.connect((args))
                return self.sock.recv(1024)
            except Exception as e:
                print(e)
       
    
    
    def do_cmd(self, obj):
        self.sock.sendall((json.dumps(obj)).encode("utf8"))
        res = self.sock.recv(1024)
        if res:
            res = json.loads(res)
            return res
        else:
            pass
        
    def close_connection(self):
        self.sock.sendall((json.dumps(['!disconnect']).encode("utf8")))
        
                   
            

class LanThread(QThread):
    connection_response = Signal(str)
    start_response = Signal(list)
    progress = Signal(int)
    
    def __init__(self, client, func, command) -> None:
        super().__init__()
        self.client = client
        self.command = command
        self.func = func
        
    def run(self):
        if self.func == 'connect':
            res = self.client.connect(self.command)
            res = res.decode('utf-8')
            self.connection_response.emit(res)

        elif self.func == 'start':
            res = self.client.do_cmd(['init',int(self.command)])
            self.start_response.emit(res)
            res = self.client.do_cmd(['hvon',int(self.command)])
            self.start_response.emit(res)
        
        elif self.func == 'set':
            res = self.client.do_cmd(['setdac',int(self.command[0]),int(self.command[1]),int(self.command[2])])
            self.start_response.emit(res)
        
        elif self.func == 'stop':
            res = self.client.do_cmd(['hvoff', int(self.command)])
            self.start_response.emit(res)

            
class LanThreadUpdate(QThread):
    response = Signal(list)
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
            #wait loop
            for i in range(self.entire_wait_time):
                if self.run_status:
                    print(i)
                    self.sleep(self.wait_time)
                else:
                    break
                
            #to faster run thread
            if not self.run_status:
                break
            
            for board in self.model.board_comlist:
                res = self.client.do_cmd(['getVT',int(board)])
                res.append(board)
                
                self.response.emit(res)
            
    
    def easy_end_thread(self):
        self.thread_start.emit(False)
        self.run_status = False
            
                
    
   
    
            
            
            
        
        
    
    

    

