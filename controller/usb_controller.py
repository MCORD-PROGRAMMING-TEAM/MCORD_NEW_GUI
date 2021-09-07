from PySide6.QtWidgets import QLineEdit


class USBController:
    def __init__(self,view,model) -> None:
        self._view = view
        self._model = model
        
        
        self.Add_ports_to_combobox()
    
    def Add_ports_to_combobox(self):
        import serial.tools.list_ports
        ports = serial.tools.list_ports.comports()
        available_ports_on =  [p.device for p in ports]
        
        self._view.ui.connection_combox.addItems(available_ports_on)
        self._view.ui.connection_combox.setCurrentIndex(-1)
        
    def set_current_device(self):
        comport = self._view.ui.connection_combox.currentText()
        self._model.comport = comport
        

        