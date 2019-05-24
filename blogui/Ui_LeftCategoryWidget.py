# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\codes\PyQt5Projects\blogui\LeftCategoryWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LeftCategoryWidget(object):
    def setupUi(self, LeftCategoryWidget):
        LeftCategoryWidget.setObjectName("LeftCategoryWidget")
        LeftCategoryWidget.resize(421, 333)
        self.vl_LeftCategoryWidget = QtWidgets.QVBoxLayout(LeftCategoryWidget)
        self.vl_LeftCategoryWidget.setContentsMargins(0, 0, 0, 0)
        self.vl_LeftCategoryWidget.setSpacing(0)
        self.vl_LeftCategoryWidget.setObjectName("vl_LeftCategoryWidget")
        self.lw_Category = QtWidgets.QListWidget(LeftCategoryWidget)
        self.lw_Category.setObjectName("lw_Category")
        self.vl_LeftCategoryWidget.addWidget(self.lw_Category)

        self.retranslateUi(LeftCategoryWidget)
        QtCore.QMetaObject.connectSlotsByName(LeftCategoryWidget)

    def retranslateUi(self, LeftCategoryWidget):
        _translate = QtCore.QCoreApplication.translate
        LeftCategoryWidget.setWindowTitle(_translate("LeftCategoryWidget", "Form"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LeftCategoryWidget = QtWidgets.QWidget()
    ui = Ui_LeftCategoryWidget()
    ui.setupUi(LeftCategoryWidget)
    LeftCategoryWidget.show()
    sys.exit(app.exec_())
