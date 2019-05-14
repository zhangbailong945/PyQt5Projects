# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Codes\PyQt5Projects\blogui\HeaderTitlebarWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HeaderTitlebarWidget(object):
    def setupUi(self, HeaderTitlebarWidget):
        HeaderTitlebarWidget.setObjectName("HeaderTitlebarWidget")
        HeaderTitlebarWidget.resize(482, 30)
        HeaderTitlebarWidget.setMaximumSize(QtCore.QSize(16777215, 40))
        HeaderTitlebarWidget.setAutoFillBackground(True)
        self.hl_htw = QtWidgets.QHBoxLayout(HeaderTitlebarWidget)
        self.hl_htw.setContentsMargins(0, 0, 0, 0)
        self.hl_htw.setSpacing(0)
        self.hl_htw.setObjectName("hl_htw")
        spacerItem = QtWidgets.QSpacerItem(279, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hl_htw.addItem(spacerItem)
        self.pb_Skin = QtWidgets.QPushButton(HeaderTitlebarWidget)
        self.pb_Skin.setMinimumSize(QtCore.QSize(40, 30))
        self.pb_Skin.setText("")
        self.pb_Skin.setObjectName("pb_Skin")
        self.hl_htw.addWidget(self.pb_Skin)
        self.pb_Minimum = QtWidgets.QPushButton(HeaderTitlebarWidget)
        self.pb_Minimum.setMinimumSize(QtCore.QSize(40, 30))
        self.pb_Minimum.setText("")
        self.pb_Minimum.setObjectName("pb_Minimum")
        self.hl_htw.addWidget(self.pb_Minimum)
        self.pb_Maximum = QtWidgets.QPushButton(HeaderTitlebarWidget)
        self.pb_Maximum.setMinimumSize(QtCore.QSize(40, 30))
        self.pb_Maximum.setText("")
        self.pb_Maximum.setObjectName("pb_Maximum")
        self.hl_htw.addWidget(self.pb_Maximum)
        self.pb_Normal = QtWidgets.QPushButton(HeaderTitlebarWidget)
        self.pb_Normal.setMinimumSize(QtCore.QSize(40, 30))
        self.pb_Normal.setText("")
        self.pb_Normal.setObjectName("pb_Normal")
        self.hl_htw.addWidget(self.pb_Normal)
        self.pb_Close = QtWidgets.QPushButton(HeaderTitlebarWidget)
        self.pb_Close.setEnabled(True)
        self.pb_Close.setMinimumSize(QtCore.QSize(40, 30))
        self.pb_Close.setText("")
        self.pb_Close.setObjectName("pb_Close")
        self.hl_htw.addWidget(self.pb_Close)

        self.retranslateUi(HeaderTitlebarWidget)
        QtCore.QMetaObject.connectSlotsByName(HeaderTitlebarWidget)

    def retranslateUi(self, HeaderTitlebarWidget):
        _translate = QtCore.QCoreApplication.translate
        HeaderTitlebarWidget.setWindowTitle(_translate("HeaderTitlebarWidget", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HeaderTitlebarWidget = QtWidgets.QWidget()
    ui = Ui_HeaderTitlebarWidget()
    ui.setupUi(HeaderTitlebarWidget)
    HeaderTitlebarWidget.show()
    sys.exit(app.exec_())

