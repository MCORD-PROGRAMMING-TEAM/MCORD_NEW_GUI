from PySide6.QtCore import  *
from PySide6.QtWidgets import *
from PySide6.QtGui import *



class QtCustomSlideButton(QCheckBox):
   
    def __init__(
        self,
        objectName = None,
        parent=None,
        witdh = 60,
        idn = None,
        active_color = '#81d3e3',
        bg_color = '#242322',
        circle_color = '#8f8c89',
        animation_curve = QEasingCurve.OutBounce,
        circle_color_active = '#fff'
    ):
        super(QtCustomSlideButton, self).__init__(parent=parent)
        #DEFULT PARAMETERS
        self.setFixedSize(witdh,28)
        self.setCursor(Qt.PointingHandCursor)
        #COLORS OF BUTTON
        self._objectName = objectName
        self._bg_color = bg_color
        self._circle_color = circle_color
        self._active_color = active_color
        self._circle_color_active = circle_color_active
        self._circle_position = 3
        self.animation = QPropertyAnimation(self,b"circle_position",self)
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(500)
        self.stateChanged.connect(self.start_transition)
        self.id = idn 
    
    #CREATE NEW SET AND GET PROPERTIE
    @Property(float)
    def circle_position(self):
        return self._circle_position
    
    @circle_position.setter
    def circle_position(self,pos):
        self._circle_position = pos
        self.update()
        
    def objectName(self) -> str:
        return self._objectName

    def start_transition(self,value):
        self.animation.stop()
        if value:
            self.animation.setEndValue(self.width() - 26)
        else:
            self.animation.setEndValue(3)
        
        self.animation.start()

        

    #ENABLE CLICK TO ALL BUTTON
    def hitButton(self,pos:QPoint):
        return self.contentsRect().contains(pos)

    #DRAW NEW ITEM
    def paintEvent(self,e):
        #ADD PAINTER
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        #NO PEN
        p.setPen(Qt.NoPen)
        
        #DRAW RECTANGLE
        rect = QRect(0,0,self.width(),self.height())

        if not self.isChecked():
            #Draw BG
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect(0,0,rect.width(),self.height(),self.height()/2,self.height()/2)

            #Draw circle
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position,3,22,22)
        else:
            #Draw BG
            p.setBrush(QColor(self._active_color))
            p.drawRoundedRect(0,0,rect.width(),self.height(),self.height()/2,self.height()/2)

            #Draw circle
            p.setBrush(QColor(self._circle_color_active))
            p.drawEllipse(self._circle_position,3,22,22)

        p.end()


