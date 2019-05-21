# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Codes\PyQt5Projects\blogui\RightSearchWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RightSearchWidget(object):
    def setupUi(self, RightSearchWidget):
        RightSearchWidget.setObjectName("RightSearchWidget")
        RightSearchWidget.resize(313, 75)
        RightSearchWidget.setAutoFillBackground(False)
        RightSearchWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(RightSearchWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb_Search_Text = QtWidgets.QLabel(RightSearchWidget)
        self.lb_Search_Text.setStyleSheet("margin-top:10px;\n"
"margin-left:10px;\n"
"")
        self.lb_Search_Text.setObjectName("lb_Search_Text")
        self.verticalLayout.addWidget(self.lb_Search_Text)
        self.lb_Search_Line = QtWidgets.QLabel(RightSearchWidget)
        self.lb_Search_Line.setMinimumSize(QtCore.QSize(0, 3))
        self.lb_Search_Line.setMaximumSize(QtCore.QSize(16777215, 9))
        self.lb_Search_Line.setStyleSheet("border:2px solid rgb(247, 155, 106);\n"
"border-left:none;\n"
"border-right:none;\n"
"border-bottom:none;\n"
"margin-top:5px;\n"
"margin-left:10px;\n"
"margin-right:10px;\n"
"")
        self.lb_Search_Line.setText("")
        self.lb_Search_Line.setObjectName("lb_Search_Line")
        self.verticalLayout.addWidget(self.lb_Search_Line)
        self.widgetSearchWidget = QtWidgets.QWidget(RightSearchWidget)
        self.widgetSearchWidget.setAutoFillBackground(False)
        self.widgetSearchWidget.setObjectName("widgetSearchWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widgetSearchWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.le_Keyword = QtWidgets.QLineEdit(self.widgetSearchWidget)
        self.le_Keyword.setMinimumSize(QtCore.QSize(0, 30))
        self.le_Keyword.setMaximumSize(QtCore.QSize(16777215, 30))
        self.le_Keyword.setStyleSheet("border:1px solid rgb(238,238,238);\n"
"margin-left:10px;\n"
"")
        self.le_Keyword.setObjectName("le_Keyword")
        self.horizontalLayout.addWidget(self.le_Keyword)
        self.pb_Keyword = QtWidgets.QPushButton(self.widgetSearchWidget)
        self.pb_Keyword.setMinimumSize(QtCore.QSize(50, 30))
        self.pb_Keyword.setStyleSheet("border:none;\n"
"background-color: rgb(247, 155, 106);\n"
"border-radius:3px;\n"
"margin-right:10px;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.pb_Keyword.setObjectName("pb_Keyword")
        self.horizontalLayout.addWidget(self.pb_Keyword)
        self.verticalLayout.addWidget(self.widgetSearchWidget)

        self.retranslateUi(RightSearchWidget)
        QtCore.QMetaObject.connectSlotsByName(RightSearchWidget)

    def retranslateUi(self, RightSearchWidget):
        _translate = QtCore.QCoreApplication.translate
        RightSearchWidget.setWindowTitle(_translate("RightSearchWidget", "Form"))
        self.lb_Search_Text.setText(_translate("RightSearchWidget", "搜索"))
        self.pb_Keyword.setText(_translate("RightSearchWidget", "搜索"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RightSearchWidget = QtWidgets.QWidget()
    ui = Ui_RightSearchWidget()
    ui.setupUi(RightSearchWidget)
    RightSearchWidget.show()
    sys.exit(app.exec_())

