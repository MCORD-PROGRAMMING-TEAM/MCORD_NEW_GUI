from PySide6.QtCore import  *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class QtCustomCirculateProgress(QWidget):
    def __init__(
        self,
        parent=None,
        progress_color = '#13a0bd',
        max_value = 100,
        suffix = '%',
        value = 20,
        width = 200,
        height = 200
        
    ):
        super(QtCustomCirculateProgress, self).__init__(parent=parent)
        self.progress_color = progress_color
        self.value = value
        self.width = width
        self.height = height
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.max_value = max_value
        self.font_size = 12
        self.suffix = suffix
        self.shadowenable = True
        self.text_color = '#fff'
        self.family_font = 'Segoe UI'
   

        # RESIZE WITHOUT LAYOUT 
        self.resize(self.width,self.height)
        self.add_shadow(self.shadowenable)
        

    def set_value(self,value):
        self.value = value
        self.repaint()

    def add_shadow(self,enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(20)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0,0,0,120))
            self.setGraphicsEffect(self.shadow)


    
    #PAINT EVENT
    def paintEvent(self, event):
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width /2
        value = self.value *360 / self.max_value

        #PAINTER
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)
        paint.setFont(QFont(self.family_font,self.font_size))

        #CREATE RECTANGLE
        rect = QRect(0,0,self.width,self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        #PEN
        pen=QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)
        
        #CREATE ARC
        paint.setPen(pen)
        paint.drawArc(margin,margin,width,height,-90*16,-value*16)

        #CREATE TEXT
        pen.setColor(QColor(self.text_color))
        paint.setPen(pen)
        paint.drawText(rect,Qt.AlignCenter,f'{self.value} {self.suffix}')

        #END
        self.show()

