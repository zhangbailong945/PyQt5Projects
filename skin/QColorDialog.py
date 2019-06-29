from PyQt5.QtCore import Qt,QSettings,QVariant,QPoint,QSize
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QPushButton,QLabel\
    ,QColorDialog
from PyQt5.QtGui import QColor
import sys,os,time
from ColourfulWidget import ColourfulWidget
from CommonUtil import Signals
from PreviewWidget import PreviewWidget
from CommonUtil import Setting
from ThemeManager import ThemeManager
from GradientUtils import GradientUtils

class MyColorDialog(QWidget):

    styleTemplate='''
    QWidget {{
            background: rgba({0}, {1}, {2}, 255);
        }}
    '''
    
    def __init__(self,*args,**kwargs):
        super(MyColorDialog,self).__init__(*args,**kwargs)
        self.setObjectName('MyQWidget')
        self.initUI()
        # 预览界面
        self.previewWidget = PreviewWidget(self)
        self.previewWidget.setVisible(False)
        # 初始化信号槽
        self._initSignals()
        colourful=Setting.value('colourful')
        if colourful:
            ThemeManager.loadFont()
            if isinstance(colourful,QColor):
                print(111)
                ThemeManager.loadColourfulTheme(colourful)
            else:
                # json数据转渐变
                print(2222)
                ThemeManager.loadColourfulTheme(
                    GradientUtils.toGradient(colourful))
        else:
            ThemeManager.loadTheme()
        
    
    def _initSignals(self):
        # 点击颜色
        Signals.colourfulItemClicked.connect(self.onColourfulItemClicked)
    
    def onColourfulItemClicked(self, name, color):
        """
        :param name:        颜色名字
        :param color:       颜色
        """
        self.skinDialog.setVisible(False)
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
        pos=Setting.value("pos",QVariant(QPoint(200,200)))
        size=Setting.value("size",QVariant(QSize(400,400)))
        styleTemplate=Setting.value('styleTemplate','\n').replace('\n','')
        self.setStyleSheet(styleTemplate)
        self.resize(size)
        self.move(pos)
    
    def showSkinDialog(self):
        self.skinDialog=ColourfulWidget()
        self.skinDialog.show()
        self.skinDialog.init()


    
    def showColorDialog(self):
        color=QColorDialog.getColor()
        if color.isValid():

            self.styleTemplate=self.styleTemplate.format(color.red(),color.green(),color.blue())
            Setting.setValue('styleTemplate',self.styleTemplate)
            styleTemplate=Setting.value('styleTemplate').replace('\n','')
            self.setStyleSheet(styleTemplate)
            
    
    def writeSettings(self):
        Setting.setValue('pos',QVariant(self.pos()))
        Setting.setValue('size',QVariant(self.size()))
    
    def closeEvent(self,event):
        self.writeSettings()
        event.accept()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=MyColorDialog()
    w.show()
    sys.exit(app.exec_())


    
