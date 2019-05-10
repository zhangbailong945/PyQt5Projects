# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Codes\PyQt5Projects\blogui\MainLayout.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainLayout(object):
    def setupUi(self, MainLayout):
        MainLayout.setObjectName("MainLayout")
        MainLayout.resize(513, 418)
        MainLayout.setAutoFillBackground(True)
        self.vl_Main = QtWidgets.QVBoxLayout(MainLayout)
        self.vl_Main.setContentsMargins(0, 0, 0, 0)
        self.vl_Main.setSpacing(0)
        self.vl_Main.setObjectName("vl_Main")
        self.topWidget = QtWidgets.QWidget(MainLayout)
        self.topWidget.setObjectName("topWidget")
        self.vl_Top = QtWidgets.QVBoxLayout(self.topWidget)
        self.vl_Top.setContentsMargins(0, 0, 0, 0)
        self.vl_Top.setSpacing(0)
        self.vl_Top.setObjectName("vl_Top")
        self.vl_Main.addWidget(self.topWidget)
        self.centerWidget = QtWidgets.QWidget(MainLayout)
        self.centerWidget.setObjectName("centerWidget")
        self.vl_Center = QtWidgets.QHBoxLayout(self.centerWidget)
        self.vl_Center.setContentsMargins(0, 0, 0, 0)
        self.vl_Center.setSpacing(0)
        self.vl_Center.setObjectName("vl_Center")
        self.leftWidget = QtWidgets.QWidget(self.centerWidget)
        self.leftWidget.setObjectName("leftWidget")
        self.vl_CenterLeft = QtWidgets.QVBoxLayout(self.leftWidget)
        self.vl_CenterLeft.setContentsMargins(0, 0, 0, 0)
        self.vl_CenterLeft.setSpacing(0)
        self.vl_CenterLeft.setObjectName("vl_CenterLeft")
        self.vl_Center.addWidget(self.leftWidget)
        self.rightWidget = QtWidgets.QWidget(self.centerWidget)
        self.rightWidget.setObjectName("rightWidget")
        self.vl_CenterRight = QtWidgets.QVBoxLayout(self.rightWidget)
        self.vl_CenterRight.setContentsMargins(0, 0, 0, 0)
        self.vl_CenterRight.setSpacing(0)
        self.vl_CenterRight.setObjectName("vl_CenterRight")
        self.vl_Center.addWidget(self.rightWidget)
        self.vl_Main.addWidget(self.centerWidget)
        self.bottomWidget = QtWidgets.QWidget(MainLayout)
        self.bottomWidget.setObjectName("bottomWidget")
        self.vl_Bottom = QtWidgets.QVBoxLayout(self.bottomWidget)
        self.vl_Bottom.setContentsMargins(0, 0, 0, 0)
        self.vl_Bottom.setSpacing(0)
        self.vl_Bottom.setObjectName("vl_Bottom")
        self.vl_Main.addWidget(self.bottomWidget)

        self.retranslateUi(MainLayout)
        QtCore.QMetaObject.connectSlotsByName(MainLayout)

    def retranslateUi(self, MainLayout):
        _translate = QtCore.QCoreApplication.translate
        MainLayout.setWindowTitle(_translate("MainLayout", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainLayout = QtWidgets.QWidget()
    ui = Ui_MainLayout()
    ui.setupUi(MainLayout)
    MainLayout.show()
    sys.exit(app.exec_())

