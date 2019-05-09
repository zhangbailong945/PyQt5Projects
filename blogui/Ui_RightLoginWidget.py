# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Codes\PyQt5Projects\blogui\RightLoginWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RightLoginWidget(object):
    def setupUi(self, RightLoginWidget):
        RightLoginWidget.setObjectName("RightLoginWidget")
        RightLoginWidget.resize(203, 82)
        RightLoginWidget.setAutoFillBackground(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(RightLoginWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb_Login_Title = QtWidgets.QLabel(RightLoginWidget)
        self.lb_Login_Title.setObjectName("lb_Login_Title")
        self.verticalLayout.addWidget(self.lb_Login_Title)
        self.lb_Login_line = QtWidgets.QLabel(RightLoginWidget)
        self.lb_Login_line.setObjectName("lb_Login_line")
        self.verticalLayout.addWidget(self.lb_Login_line)
        self.clb_Login = QtWidgets.QCommandLinkButton(RightLoginWidget)
        self.clb_Login.setObjectName("clb_Login")
        self.verticalLayout.addWidget(self.clb_Login)

        self.retranslateUi(RightLoginWidget)
        QtCore.QMetaObject.connectSlotsByName(RightLoginWidget)

    def retranslateUi(self, RightLoginWidget):
        _translate = QtCore.QCoreApplication.translate
        RightLoginWidget.setWindowTitle(_translate("RightLoginWidget", "Form"))
        self.lb_Login_Title.setText(_translate("RightLoginWidget", "TextLabel"))
        self.lb_Login_line.setText(_translate("RightLoginWidget", "TextLabel"))
        self.clb_Login.setText(_translate("RightLoginWidget", "CommandLinkButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RightLoginWidget = QtWidgets.QWidget()
    ui = Ui_RightLoginWidget()
    ui.setupUi(RightLoginWidget)
    RightLoginWidget.show()
    sys.exit(app.exec_())

