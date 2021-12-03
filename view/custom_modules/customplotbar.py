from PySide6.QtCore import QMargins, QPoint, Qt, Slot, QDateTime
from PySide6.QtGui import QBrush, QFont, QPainter, QColor
from PySide6.QtWidgets import  QWidget
from PySide6.QtCharts import QChartView, QLineSeries, QChart,QValueAxis,QDateTimeAxis


class Plot_Canvas(QWidget):
    def __init__(self) -> None:
        QWidget.__init__(self)
        self.font = QFont("Sans Serif")
        self.font.setPixelSize(14)
        self.chart = QChart()
        self.chart.setAnimationOptions(QChart.AllAnimations)
        self.chart.legend().setAlignment(Qt.AlignTop)
        self.chart.legend().setLabelColor(Qt.white)
        self.chart.legend().setFont(self.font)
        self.chart.createDefaultAxes()
        self.chart.setBackgroundVisible(False)
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setRubberBand(QChartView.ClickThroughRubberBand)
        
    
        
        
        self.create_x_axis()
        
    def create_x_axis(self):
        self.axis_x = QDateTimeAxis()
        self.axis_x.setFormat("h:mm:ss")
        self.axis_x.setLabelsAngle(70)
        self.axis_x.setTickCount(10)
        self.axis_x.setTitleText("Time of measurement")
        self.axis_x.setTitleBrush(QBrush(Qt.white))
        self.axis_x.setLabelsFont(self.font)
        self.axis_x.setMax(QDateTime.currentDateTime().addSecs(30))
        self.axis_x.setMin(QDateTime.currentDateTime())
        self.axis_x.setLabelsBrush(Qt.white)
  
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        
    def create_y_axis(self, tickcount, name, minv, maxv):
        self.axis_y = QValueAxis()
        self.axis_y.setTickCount(tickcount)
        self.axis_y.setTitleText(name)
        self.axis_y.setTitleBrush(QBrush(Qt.white))
        self.axis_y.setLabelsFont(self.font)
        self.axis_y.setRange(minv,maxv)
        self.axis_y.setLabelsBrush(Qt.white)
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        
    def create_series(self,number):
        series = QLineSeries()
        series.setName(f'Board {number}')
        series.setPointsVisible(True)
        series.setMarkerSize(4)
        
        self.chart.addSeries(series)
        series.attachAxis(self.axis_x)
        series.attachAxis(self.axis_y)
        
    def remove_series(self,number):
        for series in self.chart.series():
            if series.name() == f'Board {number}':
                print(series.name())
                self.chart.removeSeries(series)
    
        
    def add_data_to_series(self,number):
        for series in self.chart.series():
            if series.name() == f'Board {number}':
                pass
                
        
        
    def resize_axis(self,x,y,times_on_plot):
        if x > self.max_xrange:
            t_m, t_M = min(x, self.axis_x.min()), max(x, self.axis_x.max())
            self.max_xrange = t_M.addSecs(5)
            if self.firsttime > times_on_plot:
                self.min_xrange = t_m.addSecs(5)
            else:
                self.min_xrange = t_m
                
        if y > self.max_yrange  or y < self.min_yrange:
            m, M = min(y, self.axis_y.min()), max(y, self.axis_y.max())
            self.max_yrange = M + 1
            self.min_yrange = m - 1
            
        self.axis_x.setRange(self.min_xrange,self.max_xrange)
        self.axis_y.setRange(self.min_yrange ,self.max_yrange)
        self.firsttime += 1
        
        
        
    
        
        
        
    