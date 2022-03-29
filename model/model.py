
from PySide6.QtWidgets import  QCheckBox, QLineEdit, QPushButton, QFrame
from PySide6.QtCore import QObject,Signal,QMargins,QRegularExpression
from PySide6.QtGui import QIntValidator,QRegularExpressionValidator
import ipaddress
from sys import platform
import numpy as np 

#import package only for windows
try:
    from plyer import notification
except ImportError:
    pass

try:
    import notify2
except ImportError:
    pass




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
        self.active_source = None
        self.valid_ip = False #if tip IP then OK
        self.connected_lan = False # if declare IP is OK 
        self.usb_status = False
        self.temp_loop_status = False
        self.board_comlist = []
        self.all_editline_simpframe = []
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
        self.thread_update_run_status = False
        self.board_error = False
        
        
        # when dubug_mode will be able, change it to true
        self.debug_login = False
   
  

        
        
        
    #### => Get Section (Storage as model attributes)

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
        
    def get_thead_update_status(self,status):
        self.thread_update_run_status = status
       

        

    
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
            self.valid_ip = True
            return True
        except:
            self._valid_ip = False
            self.ip_error()
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
        
        
    def valid_temperature_from_raw_to_celc(self,temp):
        if not isinstance(temp,float):
            temp = float(temp)
        a0 = 1.161337
        a1 = 0.1158778
        a2 = -0.000065
        return round(a0 + a1*temp + a2*temp**2,2)
    
    def valid_voltage_from_raw(self,voltage):
        if not isinstance(voltage,int):
            voltage = int(voltage)
        
        a = 0.018392205
        b = 1.828380024
        return round(a*voltage+b,2)
    
    def valid_timer_time(self):
        if self.active_source == 'USB':
            return [90,60]
        elif self.active_source == 'LAN':
            return [50,30]
        
    def valid_powerbuttons_status(self):
        checker = [button.isChecked() for button, _ in self.all_power_buttons.values()]
        if any(checker):
            return True
        else:
            return False
        
    def valid_received_params_from_update_thread(self,params):
        board_number = params[3]
        mv, mt = params[1][0], params[1][1]
        sv, st = params[2][0], params[2][1]
        return board_number, mv, mt, sv, st 
    
    
    def valid_breakdown_voltage(self,volt,curr):
        volt = np.array(volt)
        curr = np.array(curr)
        vbr = volt[curr>0][0]   
        print(f"Vbr found at: {vbr}, operation voltage will be set: {vbr +2 }")
        return vbr + 2  
    
    #### => Set section (semi valid and set sth)
    def set_board_number_asNumber(self):
        onlyInt = QIntValidator()
        for _ , editline in self.all_power_buttons.values():
            editline.setValidator(onlyInt)
            
    def set_voltage_asNumber(self,obj):
        onlyInt_fromRange = QRegularExpressionValidator(QRegularExpression("([5-6][0-9]?\.[0-9]+)|(65\.0+)"))
        for combo in obj.findChildren(QLineEdit):
            combo.setValidator(onlyInt_fromRange)
            self.get_editline_list(combo)
            
    def set_voltage_range(self):
        min_voltage = 53.00
        max_voltage = 65.00
        
        if self.debug_login:
            min_voltage = 00.00
            max_voltage = 100.00
        
        value = float(self.sender().text())
        if min(min_voltage, max_voltage) < value < max(min_voltage, max_voltage):
            self.get_simp_status(value)
        else:
            self.error_voltage_range()
            self.sender().clear()
            self.get_simp_status(53.00)
        
    def set_working_values(self):
        self.simp_work_params[self.active_board] = [self.active_master_voltage,self.active_slave_voltage,self.active_temp]
        self.active_master_voltage = 0
        self.active_slave_voltage = 0
        
        
        
            
    ###### => Errors
    def error_no_voltage_set(self):
        title = "No voltage has been set"
        message = "Please set a voltage value once again"
        self.display_error(title,message)
        
    def connection_error(self):
        title = "Connection to HUB cannot be established"
        message = "Device is busy or ip address is incorrect"
        self.display_error(title,message)
        
    def ip_error(self):
        title = "Wrong IP address"
        message ="Please try again!"
        self.display_error(title,message)
            
    def error_voltage_range(self):
        title = "Voltage value not in work range"
        message = "Minimum voltage value (53.00 V) will be set "
        self.display_error(title,message)
        
    def error_board_number(self):
        title = "Board with provided ID is not connected to HUB"
        message = "Please check ID and try again"
        self.display_error(title,message)
        

    def display_error(self,title,message):
        if platform == 'win32':
            notification.notify(
            title = title,
            message = message,
            timeout = 5
            )
        
        elif platform == 'linux':
            notify2.init("Test")
            notice = notify2.Notification(title, message)
            notice.show()
        
        
        
        


        
        
        
        
            
        

    
    
            

        


    
