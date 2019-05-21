# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Codes\PyQt5Projects\blogui\LeftPostWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LeftPostWidget(object):
    def setupUi(self, LeftPostWidget):
        LeftPostWidget.setObjectName("LeftPostWidget")
        LeftPostWidget.resize(313, 208)
        LeftPostWidget.setAutoFillBackground(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(LeftPostWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tb_Post = QtWidgets.QTextBrowser(LeftPostWidget)
        self.tb_Post.setObjectName("tb_Post")
        self.verticalLayout.addWidget(self.tb_Post)
        self.pb_Previous = QtWidgets.QPushButton(LeftPostWidget)
        self.pb_Previous.setMinimumSize(QtCore.QSize(0, 20))
        self.pb_Previous.setAutoFillBackground(False)
        self.pb_Previous.setStyleSheet("border:none;\n"
"color:white;\n"
"background-color: rgb(247, 155, 106);\n"
"border-radius:8px;\n"
"margin-top:5px;\n"
"")
        self.pb_Previous.setObjectName("pb_Previous")
        self.verticalLayout.addWidget(self.pb_Previous)
        self.pb_Next = QtWidgets.QPushButton(LeftPostWidget)
        self.pb_Next.setMinimumSize(QtCore.QSize(0, 20))
        self.pb_Next.setAutoFillBackground(False)
        self.pb_Next.setStyleSheet("border:none;\n"
"color:white;\n"
"background-color: rgb(247, 155, 106);\n"
"border-radius:8px;\n"
"margin-top:5px;\n"
"")
        self.pb_Next.setObjectName("pb_Next")
        self.verticalLayout.addWidget(self.pb_Next)

        self.retranslateUi(LeftPostWidget)
        QtCore.QMetaObject.connectSlotsByName(LeftPostWidget)

    def retranslateUi(self, LeftPostWidget):
        _translate = QtCore.QCoreApplication.translate
        LeftPostWidget.setWindowTitle(_translate("LeftPostWidget", "Form"))
        self.pb_Previous.setText(_translate("LeftPostWidget", "上一页"))
        self.pb_Next.setText(_translate("LeftPostWidget", "下一页"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LeftPostWidget = QtWidgets.QWidget()
    ui = Ui_LeftPostWidget()
    ui.setupUi(LeftPostWidget)
    LeftPostWidget.show()
    sys.exit(app.exec_())

