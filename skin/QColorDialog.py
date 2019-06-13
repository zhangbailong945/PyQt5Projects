from PyQt5.QtCore import Qt,QSettings,QVariant,QPoint,QSize
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QPushButton,QLabel\
    ,QColorDialog
from PyQt5.QtGui import *
import sys,os,time


class MyColorDialog(QWidget):

    styleTemplate='''
    QWidget {{
            background: rgba({0}, {1}, {2}, 255);
        }}
    '''
    
    def __init__(self,*args,**kwargs):
        super(MyColorDialog,self).__init__(*args,**kwargs)
        self.initUI()

    
    def initUI(self):
        layout=QVBoxLayout()
        self.btnColor=QPushButton('选择颜色',self)
        layout.addWidget(self.btnColor)
        self.btnColor.clicked.connect(self.showColorDialog)
        self.setLayout(layout)
        self.readSettings()
    
    def readSettings(self):
        path='./settings.ini'
        if os.path.exists(path) and os.path.isfile(path):
            settings=QSettings(path,QSettings.IniFormat)
            pos=settings.value("pos",QVariant(QPoint(200,200)))
            size=settings.value("size",QVariant(QSize(400,400)))
            styleTemplate=settings.value('styleTemplate').replace('\n','')
            self.setStyleSheet(styleTemplate)
            self.resize(size)
            self.move(pos)
        else:
            return


    
    def showColorDialog(self):
        color=QColorDialog.getColor()
        if color.isValid():

            self.styleTemplate=self.styleTemplate.format(color.red(),color.green(),color.blue())
            settings=QSettings('./settings.ini',QSettings.IniFormat)
            settings.setValue('styleTemplate',self.styleTemplate)
            self.setStyleSheet(settings.value('styleTemplate'))
            
    
    def writeSettings(self):
        settings=QSettings('./settings.ini',QSettings.IniFormat)
        settings.setValue('pos',QVariant(self.pos()))
        settings.setValue('size',QVariant(self.size()))
    
    def closeEvent(self,event):
        self.writeSettings()
        event.accept()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=MyColorDialog()
    w.show()
    sys.exit(app.exec_())


    
