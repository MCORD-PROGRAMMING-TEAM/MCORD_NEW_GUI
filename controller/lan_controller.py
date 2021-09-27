from PySide6.QtCore import QThread, Signal, QWaitCondition, QMutex
import random, time


class LanController:
    def __init__(self,view,model) -> None:
        self._view = view 
        self._model = model
    
        
        
    
    def allowed_only_lan(self):
        text = self._view.ui.connection_edit.text()
        result = self._model.valid_ipaddress(text)
        if result:
            self._model.ip = text
        self._view.change_if_ip_reponse(result)
        
    ###### = > Test Thread update
 
    def check_if_thread_works(self):
        self._view.ui.worker = TestThread(self._view.ui.board_combo.currentText())
        self._view.ui.worker.start()
        self._view.ui.worker.setTerminationEnabled(True)
        self._view.ui.worker.finished.connect(self.stop_thead)
        self._view.ui.worker.update_test.connect(self._model.set_update_working_values)
        self._view.ui.worker.update_circ_test.connect(self._view.update_temp_circ)
        self._view.ui.worker.update_table.connect(self._view.update_params_table)
        self._view.ui.worker.update_text.connect(self._view.update_console)
    
    
    def stop_thead(self):
        if self._view.ui.worker.isRunning():
            print("Thread has been stoped")
            self._view.ui.worker.quit()
            
        


class TestThread(QThread):
    
    update_test = Signal(list)
    update_circ_test = Signal(int)
    update_table = Signal(list)
    update_text = Signal(str)
    
    waitCondition =QWaitCondition()
    mutex =QMutex()

    def __init__(self,board_number=9) -> None:
        super().__init__()
        self.board_number = board_number
        self.running = True
        
        
    def run(self):
        while self.running:
            self.sleep(10)
            a = round(random.uniform(53.00, 65.00), 2)
            b = round(random.uniform(53.00, 65.00), 2)
            c = round(random.uniform(25.00, 40.00), 2)
            site = random.choices(['Master','Slave'],weights=[2,1],k=1)
            result = [self.board_number,a,b,c]
            self.update_test.emit(result)
            self.update_table.emit([self.board_number,site])
            self.update_text.emit(f'Parameters has been updated')
            self.update_circ_test.emit(0)
      
        
    def stop(self):
        self.running = False
            
            
    

