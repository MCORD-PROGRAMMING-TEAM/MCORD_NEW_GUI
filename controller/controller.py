from functools import partial
from PySide6.QtCore import Qt
from controller.usb_controller import USBController
from controller.lan_controller import LanController

class Controller:
    def __init__(self,view,model) -> None:
        self._view = view
        self._model = model
        self.usbcontroller = USBController(view,model)
        self.lancontroller = LanController(view,model)
        self._constantSettings()
        self._connectToggle()
        self._applybuttonspage()
        self._runtimer()
        self._powerbuttonslogic()
        self._simpframesettingslogic()
        self._parameterslogic()
        self._frames_animation()
        self._enable_shadow_effect()
    
        
        
        
        
        
    def _connectToggle(self):
        self._view.ui.ToggleButton.clicked.connect(self._view.toggleMenu)
        self._view.ui.SettingsButton.clicked.connect(self._view.toggleMenu)
        self._view.ui.maximizeButton.clicked.connect(self._view.maximize_windowsize)
        self._view.ui.maximizeButton.clicked.connect(self._view.resize_circ_progress_bars)
        self._view.ui.closeButton.clicked.connect(self._view.close)
        self._view.ui.minimizeButton.clicked.connect(self._view.showMinimized)
        self._view.ui.usb_lan_button.stateChanged.connect(self._view.animated_changeUSB_IP)
        self._view.ui.connection_combox.currentIndexChanged.connect(self.usbcontroller.set_current_device)
        self._view.ui.connection_edit.editingFinished.connect(self.lancontroller.allowed_only_lan)
        self._model.up_or_down_progressBar_frame.connect(self._view.animated_ProgressBar_frame)
        self._view.ui.simp_combo.currentIndexChanged.connect(self._model.get_current_simp_and_board)
        self._view.ui.board_combo.currentIndexChanged.connect(self._model.get_current_simp_and_board)
     
        
    def _constantSettings(self):
        self._view.ui.titleframe.mouseMoveEvent = self.moveWindow
        self._view.splashscreen.sp.main_frame.mouseMoveEvent = self._view.splashscreen.moveWindow
        self._view.replaceWidgetsToCustom()
        self._view.Allow_Qt_timers()
        self._model.set_board_number_asNumber()
        self._model.set_voltage_asNumber(self._view.ui.Setting_frame)
        self._view.hide_frames()
        self._view.update_simp_comlist()
        
    def _enable_shadow_effect(self):
        self._view.enable_shadow_effect(self._view.ui.LeftMenuFrame,50,10,5,80)
        self._view.enable_shadow_effect(self._view.ui.background,10,5,5,80)
        self._view.enable_shadow_effect(self._view.splashscreen,10,5,5,80)
        self._view.enable_shadow_effect(self._view.splashscreen.sp.progressBar,10,5,5,80)
        self._view.enable_shadow_effect(self._view.ui.select_conn_frame,10,5,5,80)
        self._view.enable_shadow_effect(self._view.ui.PowerSupply_frame,10,5,5,80)
        self._view.enable_shadow_effect(self._view.ui.Setting_frame,10,5,5,80)
        self._view.enable_shadow_effect(self._view.ui.Parameters_frame,10,5,5,80)
        self._view.enable_shadow_effect(self._view.ui.Console_frame,10,5,5,80)
    
  
        
        
    def _powerbuttonslogic(self):
        for button, linedit in self._model.all_power_buttons.values():
            button.stateChanged.connect(self._view.PowerButtonsProgressbar)
            button.stateChanged.connect(self._view.animated_ProgressBar_frame)
            linedit.editingFinished.connect(self._model.get_all_boards)
            linedit.editingFinished.connect(self._model.get_work_params)
        
            button.stateChanged.connect(self._view.clear_board_comlist)
            button.stateChanged.connect(self._view.update_board_comlist)
    
    def _simpframesettingslogic(self):
        self._view.ui.simp_combo.currentIndexChanged.connect(self._view.animated_voltage_panels)
        self._view.ui.simp_combo.currentIndexChanged.connect(self._model.get_settings_trigger)
        for lineedit in self._model.all_editline_simpframe:
            lineedit.editingFinished.connect(self._model.set_voltage_range)
        self._view.ui.settings_button.clicked.connect(self._model.set_working_values)
        
    def _parameterslogic(self):
        self._view.ui.parameters_board_combo.activated.connect(self._view.update_progress_circ)
            

    def _applybuttonspage(self):
        self._model.get_all_menu_buttons(self._view.ui.buttonsframe)
        for button in self._model.all_menu_buttons:
            button.clicked.connect(partial(self._view.changePage,button))
            
    def _runtimer(self):
        self._view.splashscreen.timer.timeout.connect(self._view.splashscreen.progress)
        self._view.ui.powerbuttons_timer.timeout.connect(self._view.PowerButtons_ProgressBar_Update)
        
    
    def _frames_animation(self):
        self._view.ui.connection_combox.currentIndexChanged.connect(self._view.expend_frames)
        self._view.ui.connection_edit.editingFinished.connect(self._view.expend_frames)
        for button, _ in self._model.all_power_buttons.values(): button.stateChanged.connect(self._view.expend_frames)
        self._view.ui.settings_button.clicked.connect(self._view.expend_frames)
               
        
        
    def moveWindow(self,event):
        if self._view.isMaximized(): 
            self._view.maximize_restore()
        if event.buttons() == Qt.LeftButton:
            self._view.move(self._view.pos() + event.globalPos() - self._view.dragPos)
            self._view.dragPos = event.globalPos()
            event.accept()
    
            
  
            
        
    
        
    
