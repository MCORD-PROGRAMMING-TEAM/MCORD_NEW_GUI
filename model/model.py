
from PySide6.QtWidgets import  QPushButton
from PySide6.QtCore import QTimer,QObject,Signal
import ipaddress



class Model(QObject):
    #Signals
    up_or_down_progressBar_frame = Signal(str)
    
    def __init__(self) -> None:
        super().__init__()
        self.all_menu_buttons = []
        self.all_power_buttons = {}
        self.comport = 'COM3'
        self.ip = 'None'
        

    def get_all_menu_buttons(self, obj):
        for button in obj.findChildren(QPushButton):
            self.all_menu_buttons.append(button)
            
    def storage_power_buttons(self,obj):
        self.all_power_buttons[f'{obj[0].objectName()}'] = obj[0]
        
        
        

    def check_which_slide(self, obj):
        slides_and_pages = {
            'btn_hub': 1,
            'btn_statistic': 2,
            'btn_plot': 3,
            'btn_diagnostic' : 4
        }
        slidename = obj.objectName()
        return slides_and_pages[slidename]

    def validcommunication(self,status):
        if status:
            self.communicationway = 'lan'
            return (0,400)
        else:
            self.communicationway = 'usb'
            return (400,0)
            
    def valid_ipaddress(self,text):
        try:
            ipaddress.ip_address(text)
            return True
        except:
            return False
        
    def valid_Qtimer_sender(self,status):
        if status == 'PB_finished':
            return (50,0)
        else:
            return (0,50)
    
    
            

        


    #value of pressbuttonstyle
    pressedbuttonstyle = """
    border-left: 15px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 #ff9ff3, stop:0.5 rgba(85, 170, 255, 0));
    background-color: #2f3542;
    """
