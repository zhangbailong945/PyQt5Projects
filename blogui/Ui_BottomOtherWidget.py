# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Codes\PyQt5Projects\blogui\BottomOtherWidget.ui'
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
        self.label_BottomLeftText = QtWidgets.QLabel(self.widgetBottomLeft)
        self.label_BottomLeftText.setObjectName("label_BottomLeftText")
        self.verticalLayout.addWidget(self.label_BottomLeftText)
        self.label_BottomLeftLine = QtWidgets.QLabel(self.widgetBottomLeft)
        self.label_BottomLeftLine.setObjectName("label_BottomLeftLine")
        self.verticalLayout.addWidget(self.label_BottomLeftLine)
        self.horizontalLayout.addWidget(self.widgetBottomLeft)
        self.widget_BottomCenter = QtWidgets.QWidget(BottomOtherWidget)
        self.widget_BottomCenter.setAutoFillBackground(False)
        self.widget_BottomCenter.setObjectName("widget_BottomCenter")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_BottomCenter)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_BottomCenterText = QtWidgets.QLabel(self.widget_BottomCenter)
        self.label_BottomCenterText.setObjectName("label_BottomCenterText")
        self.verticalLayout_2.addWidget(self.label_BottomCenterText)
        self.label_BottomCenterLine = QtWidgets.QLabel(self.widget_BottomCenter)
        self.label_BottomCenterLine.setObjectName("label_BottomCenterLine")
        self.verticalLayout_2.addWidget(self.label_BottomCenterLine)
        self.horizontalLayout.addWidget(self.widget_BottomCenter)
        self.widget_BottomRight = QtWidgets.QWidget(BottomOtherWidget)
        self.widget_BottomRight.setAutoFillBackground(False)
        self.widget_BottomRight.setObjectName("widget_BottomRight")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_BottomRight)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_BottomRightText = QtWidgets.QLabel(self.widget_BottomRight)
        self.label_BottomRightText.setObjectName("label_BottomRightText")
        self.verticalLayout_3.addWidget(self.label_BottomRightText)
        self.label_BottomRightLine = QtWidgets.QLabel(self.widget_BottomRight)
        self.label_BottomRightLine.setObjectName("label_BottomRightLine")
        self.verticalLayout_3.addWidget(self.label_BottomRightLine)
        self.horizontalLayout.addWidget(self.widget_BottomRight)

        self.retranslateUi(BottomOtherWidget)
        QtCore.QMetaObject.connectSlotsByName(BottomOtherWidget)

    def retranslateUi(self, BottomOtherWidget):
        _translate = QtCore.QCoreApplication.translate
        BottomOtherWidget.setWindowTitle(_translate("BottomOtherWidget", "Form"))
        self.label_BottomLeftText.setText(_translate("BottomOtherWidget", "TextLabel"))
        self.label_BottomLeftLine.setText(_translate("BottomOtherWidget", "TextLabel"))
        self.label_BottomCenterText.setText(_translate("BottomOtherWidget", "TextLabel"))
        self.label_BottomCenterLine.setText(_translate("BottomOtherWidget", "TextLabel"))
        self.label_BottomRightText.setText(_translate("BottomOtherWidget", "TextLabel"))
        self.label_BottomRightLine.setText(_translate("BottomOtherWidget", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BottomOtherWidget = QtWidgets.QWidget()
    ui = Ui_BottomOtherWidget()
    ui.setupUi(BottomOtherWidget)
    BottomOtherWidget.show()
    sys.exit(app.exec_())

