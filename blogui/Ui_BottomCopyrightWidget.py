# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Codes\PyQt5Projects\blogui\BottomCopyrightWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BottomCopyrightWidget(object):
    def setupUi(self, BottomCopyrightWidget):
        BottomCopyrightWidget.setObjectName("BottomCopyrightWidget")
        BottomCopyrightWidget.resize(400, 41)
        BottomCopyrightWidget.setAutoFillBackground(False)
        BottomCopyrightWidget.setStyleSheet("background-color: rgb(17, 17, 17);\n"
"color: rgb(85, 85, 85);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(BottomCopyrightWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_BottomCopyright_Copyright = QtWidgets.QLabel(BottomCopyrightWidget)
        self.label_BottomCopyright_Copyright.setObjectName("label_BottomCopyright_Copyright")
        self.horizontalLayout.addWidget(self.label_BottomCopyright_Copyright)
        self.label_BottomCopyright_Site = QtWidgets.QLabel(BottomCopyrightWidget)
        self.label_BottomCopyright_Site.setOpenExternalLinks(True)
        self.label_BottomCopyright_Site.setObjectName("label_BottomCopyright_Site")
        self.horizontalLayout.addWidget(self.label_BottomCopyright_Site)
        self.label_BottomCopyRight_Line = QtWidgets.QLabel(BottomCopyrightWidget)
        self.label_BottomCopyRight_Line.setObjectName("label_BottomCopyRight_Line")
        self.horizontalLayout.addWidget(self.label_BottomCopyRight_Line)
        self.label_BottomCopyright_Beian = QtWidgets.QLabel(BottomCopyrightWidget)
        self.label_BottomCopyright_Beian.setOpenExternalLinks(True)
        self.label_BottomCopyright_Beian.setObjectName("label_BottomCopyright_Beian")
        self.horizontalLayout.addWidget(self.label_BottomCopyright_Beian)
        spacerItem1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(BottomCopyrightWidget)
        QtCore.QMetaObject.connectSlotsByName(BottomCopyrightWidget)

    def retranslateUi(self, BottomCopyrightWidget):
        _translate = QtCore.QCoreApplication.translate
        BottomCopyrightWidget.setWindowTitle(_translate("BottomCopyrightWidget", "Form"))
        self.label_BottomCopyright_Copyright.setText(_translate("BottomCopyrightWidget", "Copyright ©"))
        self.label_BottomCopyright_Site.setText(_translate("BottomCopyrightWidget", "LoachBlog个人笔记"))
        self.label_BottomCopyRight_Line.setText(_translate("BottomCopyrightWidget", "|"))
        self.label_BottomCopyright_Beian.setText(_translate("BottomCopyrightWidget", "粤ICP备16026304号-2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BottomCopyrightWidget = QtWidgets.QWidget()
    ui = Ui_BottomCopyrightWidget()
    ui.setupUi(BottomCopyrightWidget)
    BottomCopyrightWidget.show()
    sys.exit(app.exec_())

