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
        RightLoginWidget.setAutoFillBackground(False)
        RightLoginWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(RightLoginWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb_Login_Title = QtWidgets.QLabel(RightLoginWidget)
        self.lb_Login_Title.setAutoFillBackground(False)
        self.lb_Login_Title.setStyleSheet("margin-top:10px;\n"
"margin-left:10px;\n"
"")
        self.lb_Login_Title.setObjectName("lb_Login_Title")
        self.verticalLayout.addWidget(self.lb_Login_Title)
        self.lb_Login_line = QtWidgets.QLabel(RightLoginWidget)
        self.lb_Login_line.setMinimumSize(QtCore.QSize(0, 3))
        self.lb_Login_line.setMaximumSize(QtCore.QSize(16777215, 8))
        self.lb_Login_line.setAutoFillBackground(False)
        self.lb_Login_line.setStyleSheet("border:2px solid rgb(247, 155, 106);\n"
"border-left:none;\n"
"border-right:none;\n"
"border-bottom:none;\n"
"margin-top:5px;\n"
"margin-left:10px;\n"
"margin-right:10px;\n"
"\n"
"")
        self.lb_Login_line.setText("")
        self.lb_Login_line.setObjectName("lb_Login_line")
        self.verticalLayout.addWidget(self.lb_Login_line)
        self.clb_Login = QtWidgets.QLabel(RightLoginWidget)
        self.clb_Login.setStyleSheet("margin-top:10px;\n"
"margin-left:10px;\n"
"")
        self.clb_Login.setOpenExternalLinks(True)
        self.clb_Login.setObjectName("clb_Login")
        self.verticalLayout.addWidget(self.clb_Login)

        self.retranslateUi(RightLoginWidget)
        QtCore.QMetaObject.connectSlotsByName(RightLoginWidget)

    def retranslateUi(self, RightLoginWidget):
        _translate = QtCore.QCoreApplication.translate
        RightLoginWidget.setWindowTitle(_translate("RightLoginWidget", "Form"))
        self.lb_Login_Title.setText(_translate("RightLoginWidget", "个人中心"))
        self.clb_Login.setText(_translate("RightLoginWidget", "<html><head/><body><p><a href=\"https://loachblog.com/accounts/login/?\"><span style=\" font-size:14pt; color:#0000ff;\">登录</span></a></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RightLoginWidget = QtWidgets.QWidget()
    ui = Ui_RightLoginWidget()
    ui.setupUi(RightLoginWidget)
    RightLoginWidget.show()
    sys.exit(app.exec_())

