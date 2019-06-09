# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\codes\PyQt5Projects\blogui\test.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 476)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setStyleSheet("QScrollBar:vertical {\n"
"    background: transparent; /*背景透明*/\n"
"    width: 10px; /*宽度*/\n"
"    margin: 0px 0px 0px 0px; /**/\n"
"    padding-top: 12px; /*距离上面12px*/\n"
"    padding-bottom: 12px; /*距离底部12px*/\n"
"}\n"
"/*横向滚动条*/\n"
"QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    height: 10px; /*高度*/\n"
"    margin: 0px 0px 0px 0px;\n"
"    padding-left: 12px; /*距离左边12px*/\n"
"    padding-right: 12px; /*距离右边12px*/\n"
"}\n"
"\n"
"/*当鼠标放到纵向或者横向滚动条上面时*/\n"
"QScrollBar:vertical:hover,QScrollBar:horizontal:hover {\n"
"    background: rgba(0, 0, 0, 30); /*修改背景透明度 30*/\n"
"    border-radius: 5px; /*圆角*/\n"
"}\n"
"\n"
"/*纵向滚动条上面的滑块*/\n"
"QScrollBar::handle:vertical {\n"
"    background: rgba(0, 0, 0, 50);\n"
"    width: 10px;\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"}\n"
"/*横向滚动条上面的滑块*/\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgba(0, 0, 0, 50);\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"/*当鼠标放到滚动条滑块上面时改变透明度实现颜色的深浅变化*/\n"
"QScrollBar::handle:vertical:hover,QScrollBar::handle:horizontal:hover {\n"
"    background: rgba(0, 0, 0, 100);\n"
"}\n"
"\n"
"/*纵向滚动条下部分块*/\n"
"QScrollBar::add-page:vertical {\n"
"    width: 10px;\n"
"    background: transparent;\n"
"}\n"
"/*横向滚动条后面部分块*/\n"
"QScrollBar::add-page:horizontal {\n"
"    height: 10px;\n"
"    background: transparent;\n"
"}\n"
"/*纵向滚动条上面部分块*/\n"
"QScrollBar::sub-page:vertical {\n"
"    width: 10px;\n"
"    background: transparent;\n"
"}\n"
"/*横向滚动条左部分块*/\n"
"QScrollBar::sub-page:horizontal {\n"
"    height: 10px;\n"
"    background: transparent;\n"
"}\n"
"/*纵向滚动条顶部三角形位置*/\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 12px;\n"
"    width: 10px;\n"
"    background: transparent;\n"
"    subcontrol-position: top;\n"
"}\n"
"/*横向滚动条左侧三角形位置*/\n"
"QScrollBar::sub-line:horizontal {\n"
"    height: 10px;\n"
"    width: 12px;\n"
"    background: transparent;\n"
"    subcontrol-position: left;\n"
"}")
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
