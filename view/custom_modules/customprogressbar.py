from PySide6.QtCore import Qt,QRect,QTimer
from PySide6.QtWidgets import QWidget,QGraphicsDropShadowEffect
from PySide6.QtGui import QColor,QPainter,QPen,QFont


class QtCustomCirculateProgress(QWidget):
    def __init__(
        self,
        parent=None,
        progress_color = '#13a0bd',
        text_color = "#fff",
        bg_color = "#2f333d",
        value = 59,
        max_value = 100,
        progress_width = 10,
        suffix = '%',
        enable_bg = True,
        is_rounded = True,
        enable_text = True,
        font_size = 12,
        font_family = "Segoe UI",
        enableshadow = True
        
    ):
        super(QtCustomCirculateProgress,self).__init__(parent=parent)
        #Round Properties
        self.value = value
        self.progress_width = progress_width
        self.progress_rounded_cap = is_rounded
        self.max_value = max_value
        self.progress_timer = QTimer()
        
        #Round Frontend
        self.progress_color = progress_color
        self.enable_bg = enable_bg
        self.bg_color = bg_color
        self.shadowenable = enableshadow
        
        #Text attributes
        self.font_size = font_size
        self.suffix = suffix
        self.text_color = text_color
        self.font_family = font_family
        self.enable_text = enable_text

        
        #inner funcs
        self.add_shadow(self.shadowenable)
        self.progress_timer.timeout.connect(self.set_new_value)
        

    def set_value(self,value):
        self.progress_timer.start()
        self.new_value = value
        

        
        
    def set_new_value(self):

        if self.new_value >= self.value:
            if self.value < self.new_value:
                if self.new_value -self.value >= 1 : step = 1
                else: step = 0.01
                self.value = round(self.value + step,2)
                
                self.repaint()
            else:
                self.progress_timer.stop()
                
        else:
            if self.value > self.new_value:
                if self.value - self.new_value >= 1 : step = 1
                else: step = 0.01
                self.value = round(self.value - step,2)
               
                self.repaint()
            else:
                self.progress_timer.stop()
                
        

    def add_shadow(self,enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(20)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0,0,0,120))
            self.setGraphicsEffect(self.shadow)


    
    #PAINT EVENT
    def paintEvent(self, e):
        # SET PROGRESS PARAMETERS
        width = self.width() - self.progress_width
        height = self.height() - self.progress_width
        margin = self.progress_width / 2
        value =  self.value * 360 / self.max_value

        # PAINTER
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing) # remove pixelated edges
        paint.setFont(QFont(self.font_family, self.font_size))

        # CREATE RECTANGLE
        rect = QRect(0, 0, self.width(), self.height())
        paint.setPen(Qt.NoPen)

        # PEN
        pen = QPen()             
        pen.setWidth(self.progress_width)
        # Set Round Cap
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        # ENABLE BG
        if self.enable_bg:
            pen.setColor(QColor(self.bg_color))
            paint.setPen(pen)  
            paint.drawArc(margin, margin, width, height, 0, 360 * 16) 

        # CREATE ARC / CIRCULAR PROGRESS
        pen.setColor(QColor(self.progress_color))
        paint.setPen(pen)      
        paint.drawArc(margin, margin, width, height, -90 * 16, -value * 16)       

        # CREATE TEXT
        if self.enable_text:
            pen.setColor(QColor(self.text_color))
            paint.setPen(pen)
            paint.drawText(rect, Qt.AlignCenter, f"{round(self.value,2)}{self.suffix}")

        # END
        paint.end()


