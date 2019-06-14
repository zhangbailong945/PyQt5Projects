from PyQt5.QtCore import Qt,QSettings,QVariant,QPoint,QSize
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QPushButton,QLabel\
    ,QColorDialog
from PyQt5.QtGui import *
import sys,os,time
from ColourfulWidget import ColourfulWidget
from CommonUtil import Signals
from PreviewWidget import PreviewWidget

class MyColorDialog(QWidget):

    styleTemplate='''
    QWidget {{
            background: rgba({0}, {1}, {2}, 255);
        }}
    '''
    
    def __init__(self,*args,**kwargs):
        super(MyColorDialog,self).__init__(*args,**kwargs)
        self.initUI()
        # 预览界面
        self.previewWidget = PreviewWidget(self)
        self.previewWidget.setVisible(False)
        # 初始化信号槽
        self._initSignals()
    
    def _initSignals(self):
        # 点击颜色
        Signals.colourfulItemClicked.connect(self.onColourfulItemClicked)
    
    def onColourfulItemClicked(self, name, color):
        """
        :param name:        颜色名字
        :param color:       颜色
        """
        self.previewWidget.setVisible(True)
        self.previewWidget.setTitle(name)
        self.previewWidget.setPixmap(PreviewWidget.Color, color)


    
    def initUI(self):
        layout=QVBoxLayout()
        self.btnColor=QPushButton('选择颜色',self)
        layout.addWidget(self.btnColor)
        self.btnColor.clicked.connect(self.showColorDialog)
        self.btnSkin=QPushButton('设置皮肤',self)
        self.btnSkin.clicked.connect(self.showSkinDialog)
        layout.addWidget(self.btnSkin)
        self.setLayout(layout)
        self.readSettings()
    
    
    
    def readSettings(self):
        path='./settings.ini'
        if os.path.exists(path) and os.path.isfile(path):
            settings=QSettings(path,QSettings.IniFormat)
            pos=settings.value("pos",QVariant(QPoint(200,200)))
            size=settings.value("size",QVariant(QSize(400,400)))
            styleTemplate=settings.value('styleTemplate').replace('\n','')
            print(styleTemplate)
            self.setStyleSheet(styleTemplate)
            self.resize(size)
            self.move(pos)
        else:
            return
    
    def showSkinDialog(self):
        self.skinDialog=ColourfulWidget()
        Signals.colourfulItemClicked.connect(
        lambda name, colors: print(name, colors))
        self.skinDialog.show()
        self.skinDialog.init()


    
    def showColorDialog(self):
        color=QColorDialog.getColor()
        if color.isValid():

            self.styleTemplate=self.styleTemplate.format(color.red(),color.green(),color.blue())
            settings=QSettings('./settings.ini',QSettings.IniFormat)
            settings.setValue('styleTemplate',self.styleTemplate)
            styleTemplate=settings.value('styleTemplate').replace('\n','')
            self.setStyleSheet(styleTemplate)
            
    
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


    
