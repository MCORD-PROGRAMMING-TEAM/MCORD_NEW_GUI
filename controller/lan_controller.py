from PySide6.QtCore import QThread, Signal

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
         
    
    def create_lan_client(self):
        self.LAN = LanClient()
        self.lan_send_connect()
        
    
    def json_parser(self,obj):
        res = f'{obj[0]} : {obj[1:]}'
        self._view.update_console(res)
    
    
    def lan_send_connect(self):
        self.lan_worker = LanThread(self.LAN,'connect',(self._model.ip, 5555))
        self.lan_worker.start()
        self.lan_worker.connection_response.connect(self._view.update_console)
        self.lan_worker.finished.connect(self.lan_worker.quit)
        
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
        command = [self._model.active_board, self._model.active_master_voltage, self._model.active_slave_voltage]
        self.lan_worker = LanThread(self.LAN,'set',command)
        self.lan_worker.start()
        self.lan_worker.start_response.connect(self.json_parser)
        self.lan_worker.finished.connect(self.lan_worker.quit)
        
    def lan_send_update(self):
        self.lan_worker_update = LanThreadUpdate(self.LAN,self._model)
        self.lan_worker_update.start()
        self.lan_worker_update.response.connect(self.json_parser)
        self.lan_worker_update.response.connect(self._view.update_params_table)
       
        
           
    

        

class LanClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def connect(self,args):
        self.sock.connect((args))
        return self.sock.recv(1024)
        
    
    def do_cmd(self, obj):
        self.sock.sendall((json.dumps(obj)).encode("utf8"))
        res = self.sock.recv(1024)
        if res:
            res = json.loads(res)
            return res
        else:
            pass
        
    def __del__(self):
        self.sock.sendall((json.dumps(['!disconnect']).encode("utf8")))
        print("Disconnect from AFE")
            
            
            

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
    
    def __init__(self,client,model):
        super().__init__()
        self.client = client
        self.model = model 
        self.run_status = True
        
    def run(self):
        while self.run_status:
            self.sleep(30)
            for board in self.model.board_comlist:
                res = self.client.do_cmd(['getVT',int(board)])
                res.append(board)
                self.response.emit(res)
            
                
    
   
    
            
            
            
        
        
    
    

    

