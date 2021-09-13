
from PySide6.QtWidgets import  QCheckBox, QComboBox, QLineEdit, QPushButton, QFrame
from PySide6.QtCore import QObject,Signal,QMargins,QRegularExpression
from PySide6.QtGui import QIntValidator,QDoubleValidator,QRegularExpressionValidator
from win10toast import ToastNotifier
import ipaddress



class Model(QObject):
    #Signals
    up_or_down_progressBar_frame = Signal(str)
    
    def __init__(self) -> None:
        super().__init__()
        self.all_menu_buttons = []
        self.all_power_buttons = {}
        self.all_editline_simpframe = []
        self.board_comlist = []
        self.comport = 'COM3'
        self.ip = 'None'
        self.active_board, self.active_simp, self.active_master_voltage, self.active_slave_voltage, self.active_temp = [None,None,None,None,None]
        self.simpsettings ={
            'Master' : 'Settings_set_master_frame',
            'Slave' : 'Settings_set_slave_frame',
            'Both' : 'Settings_set_both_master_slave_frame'
        }
        self.settingstriggerd = False
        self.preview_settings_frametrigged = False
      

    def get_all_menu_buttons(self, obj):
        for button in obj.findChildren(QPushButton):
            self.all_menu_buttons.append(button)
            
    def storage_power_buttons(self,button,editext):
        self.all_power_buttons[f'{button[0].objectName()}'] = [button[0],editext[0]]
        
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
        
    def add_items_to_board_comlist(self):
        board_number = self.sender().text()
        if not self.sender().parentWidget().findChild(QCheckBox).checkState():
            self.board_comlist.append(board_number)
    
    def clear_board_comlist(self,status):
        if not status:
            board_number = self.sender().parentWidget().findChild(QLineEdit).text()
            self.board_comlist.remove(board_number)
            self.sender().parentWidget().findChild(QLineEdit).clear()

    def valid_board_number_asNumber(self):
        onlyInt = QIntValidator()
        for _ , editline in self.all_power_buttons.values():
            editline.setValidator(onlyInt)
            
    def valid_voltage_asNumber(self,frame):
        onlyInt_fromRange = QRegularExpressionValidator(QRegularExpression("([5-6][0-9]?\.[0-9]+)|(65\.0+)"))
        for combo in frame.findChildren(QLineEdit):
            combo.setValidator(onlyInt_fromRange)
            self.all_editline_simpframe.append(combo)
           
    def valid_ipaddress(self,text):
        try:
            ipaddress.ip_address(text)
            return True
        except:
            toaster = ToastNotifier()
            toaster.show_toast("Wrong IP address","Please try again!",threaded=True,duration=3)
            return False
        
    def valid_Qtimer_sender(self,status):
        if status == 'PB_finished':
            return (50,0)
        else:
            return (0,50)
        
    def set_current_simp_and_board(self):
        if self.sender().objectName() == "simp_combo":
            self.active_simp = self.sender().currentText() 
        else:
            self.active_board = self.sender().currentText()
            
    def valid_which_frame(self):
        return self.simpsettings[self.active_simp]
    
    def check_if_any_simp_settings_is_active(self,motherframe):
        for framename in self.simpsettings.values():
            if motherframe.findChild(QFrame,framename).height() > 0:
                return motherframe.findChild(QFrame,framename)
    
    def check_if_settings_has_been_ran(self):
        if isinstance(self.sender(),QComboBox):
            self.settingstriggerd = True
        if isinstance(self.sender(),QPushButton):
            self.preview_settings_frametrigged = True
            
    def check_size_frame_to_fit_circ_progressbars(self,window,circ):
        if window.isMaximized():
            circ.font_size = 18
            return QMargins(60,80,60,80)
        else:
            circ.font_size = 12
            return QMargins(40,40,40,40)  

        
            
    def valid_voltage_range(self):
        def valid_simp(value):   
            line_edit={
                'settings_master_linedit': 1, 
                'settings_slave_linedit': 0,
                'settings_set_both_slave_editline': 0,
                'settings_set_both_master_editline': 1,
            }
            if line_edit[self.sender().objectName()]:
                self.active_master_voltage = value
            else:
                self.active_slave_voltage = value
        
        value = float(self.sender().text())
        if min(53.00, 65.00) < value < max(53.00, 65.00):
            valid_simp(value)
        else:
            toaster = ToastNotifier()
            toaster.show_toast("Voltage value not in work range","Minimum voltage value (53.00 V) will be set ",threaded=True,duration=3)
            self.sender().clear()
            valid_simp(53)

        
      
        
            
        

    
    
            

        


    #value of pressbuttonstyle
    pressedbuttonstyle = """
    border-left: 15px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 #ff9ff3, stop:0.5 rgba(85, 170, 255, 0));
    background-color: #2f3542;
    """
