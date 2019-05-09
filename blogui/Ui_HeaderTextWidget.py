# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Codes\PyQt5Projects\blogui\HeaderTextWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HeaderTextWidget(object):
    def setupUi(self, HeaderTextWidget):
        HeaderTextWidget.setObjectName("HeaderTextWidget")
        HeaderTextWidget.resize(400, 81)
        HeaderTextWidget.setAutoFillBackground(True)
        self.horizontalLayout = QtWidgets.QHBoxLayout(HeaderTextWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(171, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lb_HeaderText1 = QtWidgets.QLabel(HeaderTextWidget)
        self.lb_HeaderText1.setObjectName("lb_HeaderText1")
        self.horizontalLayout.addWidget(self.lb_HeaderText1)
        self.lb_HeaderText2 = QtWidgets.QLabel(HeaderTextWidget)
        self.lb_HeaderText2.setObjectName("lb_HeaderText2")
        self.horizontalLayout.addWidget(self.lb_HeaderText2)
        spacerItem1 = QtWidgets.QSpacerItem(171, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(HeaderTextWidget)
        QtCore.QMetaObject.connectSlotsByName(HeaderTextWidget)

    def retranslateUi(self, HeaderTextWidget):
        _translate = QtCore.QCoreApplication.translate
        HeaderTextWidget.setWindowTitle(_translate("HeaderTextWidget", "Form"))
        self.lb_HeaderText1.setText(_translate("HeaderTextWidget", "Loach"))
        self.lb_HeaderText2.setText(_translate("HeaderTextWidget", "Blog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HeaderTextWidget = QtWidgets.QWidget()
    ui = Ui_HeaderTextWidget()
    ui.setupUi(HeaderTextWidget)
    HeaderTextWidget.show()
    sys.exit(app.exec_())

