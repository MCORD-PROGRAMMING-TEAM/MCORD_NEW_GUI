from signal import SIGABRT
from view.ui_main import Ui_MainWindow
from PySide6.QtWidgets import QCheckBox, QFrame, QLineEdit, QMainWindow, QGraphicsDropShadowEffect, QPushButton, QSizeGrip
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QTimer, Qt, Slot, Signal
from PySide6.QtGui import QColor, QIcon
from view.custom_modules import SlidingStackedWidget, Splashscreen ,QtCustomSlideButton


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
            self.model.storage_power_buttons(button.parentWidget().findChildren(QCheckBox),button.parentWidget().findChildren(QLineEdit))
         

        
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
        slideto = self.model.check_which_slide(button)
        self.reset_clicked_style(button)
        self.select_clicked_style(button)
        self.ui.stackedWidget.slidetowidget(slideto)
        
    
    def changeUSB_IP(self,status):
            self.animationusb = QPropertyAnimation(self.ui.connection_selection_usb, b"maximumWidth")
            self.animationusb.setDuration(200)
            self.animationusb.setEasingCurve(QEasingCurve.InElastic)
            
            self.animationlan = QPropertyAnimation(self.ui.connection_selection_lan, b"maximumWidth")
            self.animationlan.setDuration(200)
            self.animationusb.setEasingCurve(QEasingCurve.InOutQuart)
            start,end = self.model.validcommunication(status)

            self.animationusb.setStartValue(end)
            self.animationusb.setEndValue(start)
            self.animationusb.start()
            
            self.animationlan.setStartValue(start)
            self.animationlan.setEndValue(end)
            self.animationlan.start()

           
    
    def change_if_ip_reponse(self, response):
        if not response:
            self.ui.connection_edit.clear()
            
    def Allow_Qt_timers(self):
        self.ui.powerbuttons_timer = QTimer()
        
            
    def PowerButtonsProgressbar(self):
        self.ui.powerbuttons_timer.start(15)
        self.ui.PB_progress_value = 0
        
  
    def PowerButtons_ProgressBar_Update(self):
        if self.ui.PB_progress_value >= 100:
            self.ui.powerbuttons_timer.stop()
            self.ui.PB_progress_value = 0
            self.model.up_or_down_progressBar_frame.emit("PB_finished")
        self.ui.progressBar.setValue(self.ui.PB_progress_value)
        self.ui.PB_progress_value += 1
        
        
    def animated_ProgressBar_frame(self,state):
        start,end = self.model.valid_Qtimer_sender(state)
            
        self.animationprogressbar = QPropertyAnimation(self.ui.PowerButton_progressframe, b"maximumHeight")
        self.animationprogressbar.setDuration(200)
        self.animationprogressbar.setEasingCurve(QEasingCurve.InOutQuart)
        self.animationprogressbar.setStartValue(start)
        self.animationprogressbar.setEndValue(end)
        self.animationprogressbar.start()


    def update_board_comlist(self):
        self.ui.board_combo.clear()
        self.ui.board_combo.addItems(self.model.board_comlist)
        self.ui.board_combo.setCurrentIndex(-1)

    def update_simp_comlist(self):
        self.ui.simp_combo.addItems(['Master','Slave','Both'])
        self.ui.simp_combo.setCurrentIndex(-1)
        
        
    def animated_voltage_panels(self):
        checkifanyactive = self.model.check_if_any_simp_settings_is_active(self.ui.Setting_frame)
        framename = self.model.valid_which_frame()
        frame = self.ui.Setting_frame.findChild(QFrame,framename)
        
        if checkifanyactive:
            self.prevanimationframesettings = QPropertyAnimation(checkifanyactive, b"maximumHeight")
            self.prevanimationframesettings.setDuration(200)
            self.prevanimationframesettings.setEasingCurve(QEasingCurve.InOutQuart)
            self.prevanimationframesettings.setStartValue(50)
            self.prevanimationframesettings.setEndValue(0)
            self.prevanimationframesettings.start()
            
        if self.model.settingstriggerd:
            self.animationframesettings = QPropertyAnimation(self.ui.Setting_frame, b"minimumHeight")
            self.animationframesettings.setDuration(200)
            self.animationframesettings.setEasingCurve(QEasingCurve.InOutQuart)
            self.animationframesettings.setStartValue(self.ui.Setting_frame.height())
            self.animationframesettings.setEndValue(self.ui.Setting_frame.height() + 50)
            self.animationframesettings.start()
       
        self.animationframe = QPropertyAnimation(frame, b"maximumHeight")
        self.animationframe.setDuration(200)
        self.animationframe.setEasingCurve(QEasingCurve.InOutQuart)
        self.animationframe.setStartValue(0)
        self.animationframe.setEndValue(50)
        self.animationframe.start()
        
      
        
        

    
            
        
        
                
    
            

   
                
        
    
            