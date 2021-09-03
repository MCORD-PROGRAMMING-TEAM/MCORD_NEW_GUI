

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
 
            
      

