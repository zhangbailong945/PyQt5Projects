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
        RightSearchWidget.resize(309, 49)
        RightSearchWidget.setAutoFillBackground(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(RightSearchWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb_Search_Text = QtWidgets.QLabel(RightSearchWidget)
        self.lb_Search_Text.setObjectName("lb_Search_Text")
        self.verticalLayout.addWidget(self.lb_Search_Text)
        self.lb_Search_Line = QtWidgets.QLabel(RightSearchWidget)
        self.lb_Search_Line.setText("")
        self.lb_Search_Line.setObjectName("lb_Search_Line")
        self.verticalLayout.addWidget(self.lb_Search_Line)
        self.widgetSearchWidget = QtWidgets.QWidget(RightSearchWidget)
        self.widgetSearchWidget.setAutoFillBackground(True)
        self.widgetSearchWidget.setObjectName("widgetSearchWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widgetSearchWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.le_Keyword = QtWidgets.QLineEdit(self.widgetSearchWidget)
        self.le_Keyword.setObjectName("le_Keyword")
        self.horizontalLayout.addWidget(self.le_Keyword)
        self.pb_Keyword = QtWidgets.QPushButton(self.widgetSearchWidget)
        self.pb_Keyword.setObjectName("pb_Keyword")
        self.horizontalLayout.addWidget(self.pb_Keyword)
        self.verticalLayout.addWidget(self.widgetSearchWidget)

        self.retranslateUi(RightSearchWidget)
        QtCore.QMetaObject.connectSlotsByName(RightSearchWidget)

    def retranslateUi(self, RightSearchWidget):
        _translate = QtCore.QCoreApplication.translate
        RightSearchWidget.setWindowTitle(_translate("RightSearchWidget", "Form"))
        self.lb_Search_Text.setText(_translate("RightSearchWidget", "搜索"))
        self.pb_Keyword.setText(_translate("RightSearchWidget", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RightSearchWidget = QtWidgets.QWidget()
    ui = Ui_RightSearchWidget()
    ui.setupUi(RightSearchWidget)
    RightSearchWidget.show()
    sys.exit(app.exec_())

