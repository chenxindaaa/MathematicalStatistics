# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\94890\Desktop\Mathematical_Statistics\Myfiles\FenbuhanshuNihe.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FenbuhanshuNihe_Form(object):
    def setupUi(self, FenbuhanshuNihe_Form):
        FenbuhanshuNihe_Form.setObjectName("FenbuhanshuNihe_Form")
        FenbuhanshuNihe_Form.resize(751, 560)
        self.label = QtWidgets.QLabel(FenbuhanshuNihe_Form)
        self.label.setGeometry(QtCore.QRect(60, 30, 111, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(FenbuhanshuNihe_Form)
        self.lineEdit.setGeometry(QtCore.QRect(190, 30, 411, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.widget = QtWidgets.QWidget(FenbuhanshuNihe_Form)
        self.widget.setGeometry(QtCore.QRect(60, 80, 531, 151))
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(60, 80, 111, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 151, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 80, 91, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.widget_2 = QtWidgets.QWidget(FenbuhanshuNihe_Form)
        self.widget_2.setGeometry(QtCore.QRect(60, 270, 531, 151))
        self.widget_2.setObjectName("widget_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 80, 111, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(60, 20, 151, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 80, 91, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(FenbuhanshuNihe_Form)
        QtCore.QMetaObject.connectSlotsByName(FenbuhanshuNihe_Form)

    def retranslateUi(self, FenbuhanshuNihe_Form):
        _translate = QtCore.QCoreApplication.translate
        FenbuhanshuNihe_Form.setWindowTitle(_translate("FenbuhanshuNihe_Form", "分布函数拟合"))
        self.label.setText(_translate("FenbuhanshuNihe_Form", "原数据存储路径"))
        self.pushButton.setText(_translate("FenbuhanshuNihe_Form", "检验"))
        self.label_2.setText(_translate("FenbuhanshuNihe_Form", "是否服从正态分布"))
        self.pushButton_2.setText(_translate("FenbuhanshuNihe_Form", "检验"))
        self.label_3.setText(_translate("FenbuhanshuNihe_Form", "是否服从泊松分布"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FenbuhanshuNihe_Form = QtWidgets.QWidget()
    ui = Ui_FenbuhanshuNihe_Form()
    ui.setupUi(FenbuhanshuNihe_Form)
    FenbuhanshuNihe_Form.show()
    sys.exit(app.exec_())

