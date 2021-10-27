
from view.ui_main import Ui_MainWindow
from PySide6.QtWidgets import QCheckBox, QComboBox, QFrame, QLineEdit, QMainWindow, QGraphicsDropShadowEffect, QPushButton, QSizeGrip, QTableWidgetItem
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QTimer, Qt
from PySide6.QtGui import QColor, QIcon
from view.custom_modules import SlidingStackedWidget, Splashscreen ,QtCustomSlideButton,HoverButton,QtCustomCirculateProgress


class View(QMainWindow):
    def __init__(self, model) -> None:
        super(View, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = model

        self.setWindowTitle("Kruksik QT Layout")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.grip = QSizeGrip(self.ui.resizeicon)
        self.grip.setStyleSheet('background: transparent')

        self.splashscreen = Splashscreen(self)

    def toggleMenu(self, status):

        if self.sender().objectName() == 'ToggleButton':
            layout = self.ui.LeftMenuFrame
            maxExtend = 200
            standard = 60
        else:
            layout = self.ui.ExtraLeftMenuFrame
            maxExtend = 160
            standard = 0

        if not status:
            width = layout.width()

            if width == standard:
                widthToExtend = maxExtend
            else:
                widthToExtend = standard

            self.animation = QPropertyAnimation(layout, b'minimumWidth')
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthToExtend)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    def enable_shadow_effect(self, widget, blur, xoff, yoff,opa):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(blur)
        shadow.setXOffset(xoff)
        shadow.setYOffset(yoff)
        shadow.setColor(QColor(0, 0, 0, opa))
        widget.setGraphicsEffect(shadow)
       

    ###### Event func #####

    def maximize_windowsize(self):
        if not self.isMaximized():
            self.showMaximized()
            self.ui.CentralAppMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeButton.setToolTip("Restore")
            self.ui.maximizeButton.setIcon(
                QIcon(u":/icons/icons/icon_restore.png"))
            self.ui.resizeicon.hide()
        else:
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.CentralAppMargins.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeButton.setToolTip("Maximize")
            self.ui.maximizeButton.setIcon(
                QIcon(u":/icons/icons/icon_maximize.png"))
            self.ui.resizeicon.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def replaceWidgetsToCustom(self):
        #replace stackedwidget with custom 
        self.ui.stackedWidget.deleteLater()
        self.ui.stackedWidget = SlidingStackedWidget()
        self.ui.stackedWidget.setObjectName(u"stackedWidget")
        self.ui.verticalLayout_13.addWidget(self.ui.stackedWidget)
        self.ui.stackedWidget.addWidget(self.ui.home_page)
        self.ui.stackedWidget.addWidget(self.ui.hub_page)
        self.ui.stackedWidget.addWidget(self.ui.statistic_page)
        self.ui.stackedWidget.addWidget(self.ui.graph_page)
        self.ui.stackedWidget.addWidget(self.ui.diagnostic_page)

        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        
        #replace buttons to slidebuttons
        self.ui.pushre_1.deleteLater()
        self.ui.usb_lan_button = QtCustomSlideButton("Usb_Lan_Button",None,80,None,'#48dbfb','#1dd1a1','#f7f7f7')
        self.ui.horizontalLayout_7.insertWidget(1,self.ui.usb_lan_button)
        
        #replace buttons to powersupplyframe
        for number,button in enumerate(self.ui.PowerButton_body.findChildren(QPushButton),start=1):
            button.deleteLater()
            exec(f"self.ui.powerbutton_{number} = QtCustomSlideButton('PowerButton_{number}',None,60,None,'#1dd1a1','#ff6b6b','#c8d6e5')")
            layout = button.parentWidget().layout().objectName()
            exec(f"self.ui.{layout}.insertWidget(2,self.ui.powerbutton_{number})")
            # Add buttons to dict in model 
            self.model.get_all_power_buttons(button.parentWidget().findChildren(QCheckBox),button.parentWidget().findChildren(QLineEdit))
            
        #replace pushbutton to hover button
        self.ui.settings_button.deleteLater()
        self.ui.settings_button = HoverButton("Set Voltage")
        self.ui.settings_button.setEnabled(False)
        self.ui.settings_choice_layout.insertWidget(4,self.ui.settings_button)
        
        
        # Add progressbars to frames
        self.ui.master_progressbar = QtCustomCirculateProgress(progress_color='#f368e0',max_value=100,suffix=' V',value=0)
        self.ui.master_layout.addWidget(self.ui.master_progressbar)
        
        self.ui.slave_progressbar = QtCustomCirculateProgress(progress_color='#54a0ff',max_value=100,suffix=' V',value=0)
        self.ui.slave_layout.addWidget(self.ui.slave_progressbar)
        
        self.ui.temperature_progressbar = QtCustomCirculateProgress(progress_color='#1dd1a1',max_value=100,suffix=' °C',value=0)
        self.ui.temperature_layout.addWidget(self.ui.temperature_progressbar)
        
        
        
    def resize_circ_progress_bars(self):
        proper_size, font_size = self.model.valid_windows_size(self.isMaximized())
        self.ui.master_layout.setContentsMargins(proper_size)
        self.ui.slave_layout.setContentsMargins(proper_size)
        self.ui.temperature_layout.setContentsMargins(proper_size)
        
        self.ui.master_progressbar.font_size = font_size
        self.ui.slave_progressbar.font_size = font_size
        self.ui.temperature_progressbar.font_size = font_size

        
    def change_clicked_button_layout(self,buttonstyle):
        new_layout = buttonstyle + self.model.pressedbuttonstyle
        return new_layout
    
    def rechange_clicked_button_layout(self,buttonstyle):
        relayout = buttonstyle.replace(self.model.pressedbuttonstyle, "")
        return relayout
    
    def select_clicked_style(self, button):
        for b in self.ui.buttonsframe.findChildren(QPushButton):
            if b.objectName() == button.objectName():
                b.setStyleSheet(self.change_clicked_button_layout(b.styleSheet()))
    
    def reset_clicked_style(self, button):
        for b in self.ui.buttonsframe.findChildren(QPushButton):
            if b.objectName() != button.objectName():
                b.setStyleSheet(self.rechange_clicked_button_layout(b.styleSheet()))
    
    
    def changePage(self, button):
        slideto = self.model.valid_wheretoSlide(button)
        self.reset_clicked_style(button)
        self.select_clicked_style(button)
        self.ui.stackedWidget.slidetowidget(slideto)
           
    
    def change_if_ip_reponse(self, response):
        if not response:
            self.ui.connection_edit.clear()
            
    def Allow_Qt_timers(self):
        self.ui.powerbuttons_timer = QTimer()
        self.ui.powerbuttons_timer.setObjectName("Power")
        self.ui.settings_timer = QTimer()
        self.ui.settings_timer.setObjectName("Settings")
        self.ui.connection_timer = QTimer(ObjectName="Connection")
        #self.ui.connection_timer.setObjectName("Connection")
        
        
            
    def Timers_start(self):
        if isinstance(self.sender(),HoverButton):
            time = self.model.valid_timer_time()
            self.ui.settings_timer.start(15)
            self.ui.settings_timer.setInterval(time[1])
        elif isinstance(self.sender(),QComboBox) or isinstance(self.sender(),QLineEdit):
            if self.model.valid_ip or self.model.usb_status:
                self.ui.connection_timer.start(15)
                self.ui.connection_timer.setInterval(10)
        else:
            time = self.model.valid_timer_time()
            print(time)
            self.ui.powerbuttons_timer.start(15)
            self.ui.powerbuttons_timer.setInterval(time[0])
        self.ui.PB_progress_value = 0
        
    
        
  
    def Progress_bars_update(self):
        progressbar, timer_name = self.model.valid_trigged_progressbar(self,self.sender().objectName())
        emitter = self.model.valid_which_signal(timer_name)

        if self.ui.PB_progress_value >= 100:
            self.sender().stop()
            self.ui.PB_progress_value = 0
            emitter.emit("PB_finished")
 
        progressbar.setValue(self.ui.PB_progress_value)
        self.ui.PB_progress_value += 1
       
        

    def update_board_comlist(self):
        self.ui.board_combo.clear()
        self.ui.parameters_board_combo.clear()
        self.ui.board_combo.addItems(self.model.board_comlist)
        self.ui.parameters_board_combo.addItems(self.model.board_comlist)
    
        
        
    def clear_board_comlist(self,status):
        if not status:
            try:
                board_number = self.sender().parentWidget().findChild(QLineEdit).text()
                self.model.current_board_number = board_number
                self.model.board_comlist.remove(board_number)
                self.sender().parentWidget().findChildren(QLineEdit)
                self.ui.settings_set_both_master_editline.clear()
                self.ui.settings_set_both_slave_editline.clear()
                self.ui.settings_master_linedit.clear()
                self.ui.settings_slave_linedit.clear()
            except:
                pass

    def update_simp_comlist(self):
        self.ui.simp_combo.addItems(['Master','Slave','Both'])
        self.ui.simp_combo.setCurrentIndex(-1)
        
        
    def apply_animation(self,obj,attribute,time,start,end):
        animation = QPropertyAnimation(obj,attribute)
        animation.setDuration(time)
        animation.setEasingCurve(QEasingCurve.InOutQuart)
        animation.setStartValue(start)
        animation.setEndValue(end)
        animation.start()
        return animation    
        
        
    def animated_ProgressBar_PowerSuply_frame(self,state):
        start,end = self.model.valid_Qtimer_sender(state)
        self.animationprogressbarpowersupply = self.apply_animation(self.ui.PowerButton_progressframe,b"maximumHeight",200,start,end)
        
    def animated_ProgressBar_Settings_frame(self,state):
        start,end = self.model.valid_Qtimer_sender(state)
        self.animationprogressbarsettings = self.apply_animation(self.ui.Settings_progress_bar_frame,b"maximumHeight",200,start,end)
        
    def animated_ProgressBar_Connection_frame(self,*state):
        if self.model.valid_ip or self.model.usb_status:
            if not any(state): state = self.model.ip_passed_status
            start,end = self.model.valid_Qtimer_sender(state[0])
            self.animationprogressbarconnection = self.apply_animation(self.ui.connection_progressbar_frame,b"maximumHeight",200,start,end)
        
    
    def unlocked_settings_button(self):
        board_status = self.model.board_changed
        if board_status:
            self.ui.settings_button.setEnabled(True)
        
    def animated_voltage_panels(self):
        checkifanyactive = self.model.valid_any_simp_settings_is_active(self.ui.Setting_frame)
        framename = self.model.valid_which_frame()
        frame = self.ui.Setting_frame.findChild(QFrame,framename)
        
        if checkifanyactive:
            self.prev_animation_settings_frame = self.apply_animation(checkifanyactive,b"maximumHeight",200,self.ui.Up_frame.width(),0)
    
        if not self.model.settingstriggerd:
            self.ui.frame.deleteLater()
            
        self.animation_settings_frame = self.apply_animation(frame,b"maximumHeight",200,0,self.ui.Up_frame.width())
        
        
    def animated_changeUSB_IP(self,status):
        start,end = self.model.valid_communicationWay(status)
        self.animationusb = self.apply_animation(self.ui.connection_selection_usb,b"maximumWidth",400,end,start)
        self.animationlan = self.apply_animation(self.ui.connection_selection_lan,b"maximumWidth",400,start,end)
           
        
    def hide_frames(self):
        for frame in [self.ui.PowerSupply_frame,self.ui.Setting_frame,self.ui.Console_frame,self.ui.Parameters_frame]:
            frame.hide()
            
            
    ##### => extend block (split into 3 coz signal emit class Model)
    def expend_frames_Settings(self):
        self.ui.Setting_frame.showNormal()
        self.ui.Console_frame.showNormal()
        
    def expend_frames_Parameters(self):
        self.ui.Parameters_frame.showNormal()
        
    def expend_frames_PowerSupply(self):
        self.ui.PowerSupply_frame.showNormal()
        
           
    
    def update_progress_circ(self):
        board_combo = self.ui.parameters_board_combo.currentText()
        print(f'What should be circ {self.model.simp_work_params[board_combo]}')
        if board_combo == '':
            board_combo = self.ui.board_combo.currentText()
        error = False
        for value, pb in enumerate(self.ui.Parameter_preview_frame.findChildren(QtCustomCirculateProgress)):
            try: 
                pb.set_value(self.model.simp_work_params[board_combo][value])
            except:
                error = True
                pb.set_value(0)
        if error: self.model.error_no_voltage_set()
        
        
    def update_temp_circ(self):
        board_combo = self.ui.parameters_board_combo.currentText()
        self.ui.temperature_progressbar.set_value(self.model.simp_work_params[board_combo][2])
        
        
    def update_console(self,text):
        self.ui.console.insertPlainText(f'>>> {text}\n')
        
    
    
    def update_params_table(self,params):
        self.found = False
        board_number = params[3]
        mv, mt = params[1][0], params[1][1]
        sv, st = params[2][0], params[2][1]
        avetemp = int(( float(mt) + float(st)) / 2)
        self.model.simp_work_params[board_number][2] = self.model.valid_temperature_from_raw_to_celc(avetemp)
        self.update_temp_circ()
        
        mt = str(self.model.valid_temperature_from_raw_to_celc(mt))
        st = str(self.model.valid_temperature_from_raw_to_celc(st))
        
        mv = str(self.model.valid_voltage_from_raw(mv))
        sv = str(self.model.valid_voltage_from_raw(sv))
        
        rdy_table_params_master = [board_number,'Master',mv,mt]
        rdy_table_params_slave = [board_number,'Slave',sv,st]
        
        where = self.ui.SIMP_details_table.findItems(board_number,Qt.MatchExactly)
        if where:
            print('Znaleziono')
            for whererow in where:
                row = whererow.row()
                if self.ui.SIMP_details_table.item(row,1).text() == 'Master':
                    itemv = QTableWidgetItem(mv)
                    itemt = QTableWidgetItem(mt)
                    itemv.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
                    itemt.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
                    self.ui.SIMP_details_table.setItem(row,2,itemv)
                    self.ui.SIMP_details_table.setItem(row,3,itemt)
                    print("Update MASTER")
                    self.found = True
                else: 
                    itemv = QTableWidgetItem(sv)
                    itemt = QTableWidgetItem(st)
                    itemv.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
                    itemt.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
                    self.ui.SIMP_details_table.setItem(row,2,itemv)
                    self.ui.SIMP_details_table.setItem(row,3,itemt)
                    print("Update SLAVE")
                    self.found = True
    
                
        else:
            print('Dodaje')
            rowcounts = self.ui.SIMP_details_table.rowCount()
            self.ui.SIMP_details_table.insertRow(rowcounts)
        
            for i, value in enumerate(rdy_table_params_master):
                item = QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
                self.ui.SIMP_details_table.setItem(rowcounts,i,item)
                
            rowcounts = self.ui.SIMP_details_table.rowCount()
            self.ui.SIMP_details_table.insertRow(rowcounts)
            
            for i, value in enumerate(rdy_table_params_slave):
                item = QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
                self.ui.SIMP_details_table.setItem(rowcounts,i,item)
                
    def remove_from_table(self,status):
        if not status:
            simp_off = self.sender().parentWidget().findChild(QLineEdit).text()
            where = self.ui.SIMP_details_table.findItems(simp_off,Qt.MatchExactly)
            for whe in where:
                row = whe.row()
                self.ui.SIMP_details_table.removeRow(row)
        
                
            
        
        
                    
            
            

            
        
    
            
            
        

        
      
        
        

    
            
        
        
                
    
            

   
                
        
    
            