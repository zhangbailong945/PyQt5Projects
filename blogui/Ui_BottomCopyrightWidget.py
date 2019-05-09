# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Codes\PyQt5Projects\blogui\BottomCopyrightWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bottomCopyrightWidget(object):
    def setupUi(self, bottomCopyrightWidget):
        bottomCopyrightWidget.setObjectName("bottomCopyrightWidget")
        bottomCopyrightWidget.resize(400, 41)
        bottomCopyrightWidget.setAutoFillBackground(False)
        bottomCopyrightWidget.setStyleSheet("background-color: rgb(17, 17, 17);\n"
"color: rgb(85, 85, 85);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(bottomCopyrightWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_BottomCopyright_Copyright = QtWidgets.QLabel(bottomCopyrightWidget)
        self.label_BottomCopyright_Copyright.setObjectName("label_BottomCopyright_Copyright")
        self.horizontalLayout.addWidget(self.label_BottomCopyright_Copyright)
        self.label_BottomCopyright_Site = QtWidgets.QLabel(bottomCopyrightWidget)
        self.label_BottomCopyright_Site.setOpenExternalLinks(True)
        self.label_BottomCopyright_Site.setObjectName("label_BottomCopyright_Site")
        self.horizontalLayout.addWidget(self.label_BottomCopyright_Site)
        self.label_BottomCopyRight_Line = QtWidgets.QLabel(bottomCopyrightWidget)
        self.label_BottomCopyRight_Line.setObjectName("label_BottomCopyRight_Line")
        self.horizontalLayout.addWidget(self.label_BottomCopyRight_Line)
        self.label_BottomCopyright_Beian = QtWidgets.QLabel(bottomCopyrightWidget)
        self.label_BottomCopyright_Beian.setOpenExternalLinks(True)
        self.label_BottomCopyright_Beian.setObjectName("label_BottomCopyright_Beian")
        self.horizontalLayout.addWidget(self.label_BottomCopyright_Beian)
        spacerItem1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(bottomCopyrightWidget)
        QtCore.QMetaObject.connectSlotsByName(bottomCopyrightWidget)

    def retranslateUi(self, bottomCopyrightWidget):
        _translate = QtCore.QCoreApplication.translate
        bottomCopyrightWidget.setWindowTitle(_translate("bottomCopyrightWidget", "Form"))
        self.label_BottomCopyright_Copyright.setText(_translate("bottomCopyrightWidget", "Copyright ©"))
        self.label_BottomCopyright_Site.setText(_translate("bottomCopyrightWidget", "LoachBlog个人笔记"))
        self.label_BottomCopyRight_Line.setText(_translate("bottomCopyrightWidget", "|"))
        self.label_BottomCopyright_Beian.setText(_translate("bottomCopyrightWidget", "粤ICP备16026304号-2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bottomCopyrightWidget = QtWidgets.QWidget()
    ui = Ui_bottomCopyrightWidget()
    ui.setupUi(bottomCopyrightWidget)
    bottomCopyrightWidget.show()
    sys.exit(app.exec_())

