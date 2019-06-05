# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\codes\PyQt5Projects\blogui\BottomOtherWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BottomOtherWidget(object):
    def setupUi(self, BottomOtherWidget):
        BottomOtherWidget.setObjectName("BottomOtherWidget")
        BottomOtherWidget.resize(400, 226)
        BottomOtherWidget.setAutoFillBackground(False)
        BottomOtherWidget.setStyleSheet("background-color: rgb(32, 32, 32);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(BottomOtherWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widgetBottomLeft = QtWidgets.QWidget(BottomOtherWidget)
        self.widgetBottomLeft.setAutoFillBackground(False)
        self.widgetBottomLeft.setObjectName("widgetBottomLeft")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widgetBottomLeft)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout.addWidget(self.widgetBottomLeft)
        self.widget_BottomCenter = QtWidgets.QWidget(BottomOtherWidget)
        self.widget_BottomCenter.setAutoFillBackground(False)
        self.widget_BottomCenter.setObjectName("widget_BottomCenter")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_BottomCenter)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout.addWidget(self.widget_BottomCenter)
        self.widget_BottomRight = QtWidgets.QWidget(BottomOtherWidget)
        self.widget_BottomRight.setAutoFillBackground(False)
        self.widget_BottomRight.setObjectName("widget_BottomRight")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_BottomRight)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout.addWidget(self.widget_BottomRight)

        self.retranslateUi(BottomOtherWidget)
        QtCore.QMetaObject.connectSlotsByName(BottomOtherWidget)

    def retranslateUi(self, BottomOtherWidget):
        _translate = QtCore.QCoreApplication.translate
        BottomOtherWidget.setWindowTitle(_translate("BottomOtherWidget", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BottomOtherWidget = QtWidgets.QWidget()
    ui = Ui_BottomOtherWidget()
    ui.setupUi(BottomOtherWidget)
    BottomOtherWidget.show()
    sys.exit(app.exec_())

