
from os import name
from PySide6.QtWidgets import  QCheckBox, QLineEdit, QPushButton, QFrame
from PySide6.QtCore import QObject,Signal,QMargins,QRegularExpression
from PySide6.QtGui import QIntValidator,QRegularExpressionValidator
from win10toast import ToastNotifier
import ipaddress



class Model(QObject):
    #Signals
    up_or_down_powersupply_progressBar_frame = Signal(str)
    up_or_down_settings_progressBar_frame = Signal(str)
    up_or_down_connection_progressBar_frame = Signal(str)
    
    
    #value of pressbuttonstyle
    pressedbuttonstyle = """
    border-left: 15px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 #ff9ff3, stop:0.5 rgba(85, 170, 255, 0));
    background-color: #2f3542;
    """
    
    def __init__(self) -> None:
        super().__init__()
        self.all_menu_buttons = []
        self.all_power_buttons = {}
        self.simp_work_params = {}
        self.simp_work_update_params = {}
        self.board_comlist = []
        self.all_editline_simpframe = []
        self.active_source = None
        self.comport = 'COM3'
        self.ip = 'None'
        self.active_board, self.active_simp, self.active_master_voltage, self.active_slave_voltage, self.active_temp = 0,0,0,0,0
        self.simpsettings ={
            'Master' : 'Settings_set_master_frame',
            'Slave' : 'Settings_set_slave_frame',
            'Both' : 'Settings_set_both_master_slave_frame'
        }
        self.settingstriggerd = False
        self.preview_settings_frametrigged = False
        self.ip_passed_status = (0,0)
        self.board_changed, self.simp_voltage_changed = False, False
  
        

    
        
        
        
    #### => Get Section (Storage as model attributes)
    def get_active_connection_source(self):
        pass

    
    def get_all_menu_buttons(self, obj):
        for button in obj.findChildren(QPushButton):
            self.all_menu_buttons.append(button)
            
    def get_all_power_buttons(self,button,editext):
        self.all_power_buttons[f'{button[0].objectName()}'] = [button[0],editext[0]]
        
    def get_all_boards(self):
        board_number = self.sender().text()
        if not self.sender().parentWidget().findChild(QCheckBox).checkState():
            self.board_comlist.append(board_number)
            self.active_board = board_number
                    
    def get_current_simp_and_board(self):
        if self.sender().objectName() == "simp_combo":
            self.active_simp = self.sender().currentText() 
        else:
            self.active_board = self.sender().currentText()
            
    def get_settings_trigger(self):
        self.settingstriggerd = True
        
    def get_simp_status(self,value):   
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
        
    
    def get_editline_list(self,item):
        self.all_editline_simpframe.append(item)
    
    def get_work_params(self):
        key = self.sender().text()
        self.simp_work_params[key] = []
        
    def get_changed_board(self):
        self.board_changed = True

        

    
    #### => valid section (Check and return)
    def valid_wheretoSlide(self, obj):
        slides_and_pages = {
            'btn_hub': 1,
            'btn_statistic': 2,
            'btn_plot': 3,
            'btn_diagnostic' : 4
        }
        slidename = obj.objectName()
        return slides_and_pages[slidename]

    def valid_communicationWay(self,status):
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
            toaster = ToastNotifier()
            toaster.show_toast("Wrong IP address","Please try again!",threaded=True,duration=3)
            return False
        
    def valid_Qtimer_sender(self,status):
        if status == 'PB_finished':
            return (50,0)
        else:
            return (0,50)
            
    def valid_which_frame(self):
        return self.simpsettings[self.active_simp]
    
    def valid_any_simp_settings_is_active(self,motherframe):
        for framename in self.simpsettings.values():
            if motherframe.findChild(QFrame,framename).height() > 0:
                return motherframe.findChild(QFrame,framename)
            
    def valid_windows_size(self,state):
        if state:
            return QMargins(60,80,60,80), 18
        else:
            return QMargins(40,40,40,40), 12
        
    def valid_expending_frame(self,obj):
        
        if "button_frame" in obj:
            obj = "button"
        
        whichframe = {
            "connection_selection_usb" : ["self.ui.PowerSupply_frame"],
            "connection_selection_lan" : ["self.ui.PowerSupply_frame"],
            "button" : ["self.ui.Setting_frame", "self.ui.Console_frame"],
            "Setting_choice_frame":["self.ui.Parameters_frame"]
        }
        
        return whichframe[obj]
    
    def valid_trigged_progressbar(self,view,obj):
        progress_bar_dict ={
            'Power' : view.ui.powersupply_progressbar,
            'Settings': view.ui.Settings_progess_bar,
            'Connection': view.ui.connection_progressbar
        }
        return progress_bar_dict[obj],obj

    def valid_which_signal(self,obj):
        if obj == "Power":
            return self.up_or_down_powersupply_progressBar_frame
        elif obj == "Settings":
            return self.up_or_down_settings_progressBar_frame
        else:
            return self.up_or_down_connection_progressBar_frame
    
    #### => Set section (semi valid and set sth)
    def set_board_number_asNumber(self):
        onlyInt = QIntValidator()
        for _ , editline in self.all_power_buttons.values():
            editline.setValidator(onlyInt)
            
    def set_voltage_asNumber(self,obj):
        onlyInt_fromRange = QRegularExpressionValidator(QRegularExpression("([1-6][0-9]?\.[0-9]+)|(65\.0+)"))
        for combo in obj.findChildren(QLineEdit):
            combo.setValidator(onlyInt_fromRange)
            self.get_editline_list(combo)
            
    def set_voltage_range(self):
        value = float(self.sender().text())
        if min(50.00, 65.00) < value < max(50.00, 65.00):
            self.get_simp_status(value)
        else:
            toaster = ToastNotifier()
            toaster.show_toast("Voltage value not in work range","Minimum voltage value (53.00 V) will be set ",threaded=True,duration=3)
            self.sender().clear()
            self.get_simp_status(53.00)
        
    def set_working_values(self):
        self.simp_work_params[self.active_board] = [self.active_master_voltage,self.active_slave_voltage,self.active_temp]
        
        
    def set_update_working_values(self,parameters):
        self.simp_work_params[parameters[0]][2] = parameters[3]
        self.simp_work_update_params[parameters[0]] = [parameters[1],parameters[2],parameters[3]]


    
    
            
    ###### => Errors
    def error_no_voltage_set(self):
        toaster = ToastNotifier()
        toaster.show_toast("No voltage has been set","Please set a voltage value once again",threaded=True,duration=3)
        
        


        
        
        
        
            
        

    
    
            

        


    
