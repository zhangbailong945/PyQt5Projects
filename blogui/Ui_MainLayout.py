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
        self.verticalLayout = QtWidgets.QVBoxLayout(MainLayout)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topWidget = QtWidgets.QWidget(MainLayout)
        self.topWidget.setObjectName("topWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.topWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addWidget(self.topWidget)
        self.centerWidget = QtWidgets.QWidget(MainLayout)
        self.centerWidget.setObjectName("centerWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centerWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftWidget = QtWidgets.QWidget(self.centerWidget)
        self.leftWidget.setObjectName("leftWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.leftWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout.addWidget(self.leftWidget)
        self.rightWidget = QtWidgets.QWidget(self.centerWidget)
        self.rightWidget.setObjectName("rightWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.rightWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout.addWidget(self.rightWidget)
        self.verticalLayout.addWidget(self.centerWidget)
        self.bottomWidget = QtWidgets.QWidget(MainLayout)
        self.bottomWidget.setObjectName("bottomWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.bottomWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout.addWidget(self.bottomWidget)

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

