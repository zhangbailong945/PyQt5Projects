# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Codes\PyQt5Projects\blogui\HeaderMenuWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HeaderMenuWidget(object):
    def setupUi(self, HeaderMenuWidget):
        HeaderMenuWidget.setObjectName("HeaderMenuWidget")
        HeaderMenuWidget.resize(400, 40)
        HeaderMenuWidget.setAutoFillBackground(True)
        self.horizontalLayout = QtWidgets.QHBoxLayout(HeaderMenuWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pb_Index = QtWidgets.QPushButton(HeaderMenuWidget)
        self.pb_Index.setMinimumSize(QtCore.QSize(50, 40))
        self.pb_Index.setCheckable(True)
        self.pb_Index.setChecked(True)
        self.pb_Index.setAutoExclusive(True)
        self.pb_Index.setObjectName("pb_Index")
        self.horizontalLayout.addWidget(self.pb_Index)
        self.pb_Category = QtWidgets.QPushButton(HeaderMenuWidget)
        self.pb_Category.setMinimumSize(QtCore.QSize(50, 40))
        self.pb_Category.setCheckable(True)
        self.pb_Category.setAutoExclusive(True)
        self.pb_Category.setObjectName("pb_Category")
        self.horizontalLayout.addWidget(self.pb_Category)
        self.pb_DateTime = QtWidgets.QPushButton(HeaderMenuWidget)
        self.pb_DateTime.setMinimumSize(QtCore.QSize(50, 40))
        self.pb_DateTime.setCheckable(True)
        self.pb_DateTime.setAutoExclusive(True)
        self.pb_DateTime.setObjectName("pb_DateTime")
        self.horizontalLayout.addWidget(self.pb_DateTime)
        self.pb_Tags = QtWidgets.QPushButton(HeaderMenuWidget)
        self.pb_Tags.setMinimumSize(QtCore.QSize(50, 40))
        self.pb_Tags.setAutoFillBackground(True)
        self.pb_Tags.setCheckable(True)
        self.pb_Tags.setChecked(False)
        self.pb_Tags.setAutoExclusive(True)
        self.pb_Tags.setObjectName("pb_Tags")
        self.horizontalLayout.addWidget(self.pb_Tags)
        self.pb_About = QtWidgets.QPushButton(HeaderMenuWidget)
        self.pb_About.setMinimumSize(QtCore.QSize(50, 40))
        self.pb_About.setCheckable(True)
        self.pb_About.setAutoRepeat(False)
        self.pb_About.setAutoExclusive(True)
        self.pb_About.setObjectName("pb_About")
        self.horizontalLayout.addWidget(self.pb_About)
        spacerItem1 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(HeaderMenuWidget)
        QtCore.QMetaObject.connectSlotsByName(HeaderMenuWidget)

    def retranslateUi(self, HeaderMenuWidget):
        _translate = QtCore.QCoreApplication.translate
        HeaderMenuWidget.setWindowTitle(_translate("HeaderMenuWidget", "Form"))
        self.pb_Index.setText(_translate("HeaderMenuWidget", "首页"))
        self.pb_Category.setText(_translate("HeaderMenuWidget", "分类"))
        self.pb_DateTime.setText(_translate("HeaderMenuWidget", "时间轴"))
        self.pb_Tags.setText(_translate("HeaderMenuWidget", "标签云"))
        self.pb_About.setText(_translate("HeaderMenuWidget", "关于"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HeaderMenuWidget = QtWidgets.QWidget()
    ui = Ui_HeaderMenuWidget()
    ui.setupUi(HeaderMenuWidget)
    HeaderMenuWidget.show()
    sys.exit(app.exec_())

