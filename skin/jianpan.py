from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QGradient,QLinearGradient,QRadialGradient,QConicalGradient
import sys

class MyWidget(QWidget):
    
    def __init__(self,*args,**kwargs):
        super(MyWidget,self).__init__(*args,**kwargs)
    
    def paintEvent(self,event):
        painter=QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing,True)
        linear=QLinearGradient(100,100,300,100)
        linear.setColorAt(0,Qt.red)
        linear.setColorAt(1,Qt.blue)
        painter.setBrush(linear)
        painter.setPen(Qt.transparent)
        painter.drawRect(100,100,100,100)

        
        

if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=MyWidget()
    w.show()
    sys.exit(app.exec_())

