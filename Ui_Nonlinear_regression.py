# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\94890\Desktop\Mathematical_Statistics\Myfiles\Nonlinear_regression.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Nonlinear_regression_Form(object):
    def setupUi(self, Nonlinear_regression_Form):
        Nonlinear_regression_Form.setObjectName("Nonlinear_regression_Form")
        Nonlinear_regression_Form.resize(926, 703)
        self.pushButton_7 = QtWidgets.QPushButton(Nonlinear_regression_Form)
        self.pushButton_7.setGeometry(QtCore.QRect(310, 220, 93, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_6 = QtWidgets.QPushButton(Nonlinear_regression_Form)
        self.pushButton_6.setGeometry(QtCore.QRect(170, 220, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_3 = QtWidgets.QPushButton(Nonlinear_regression_Form)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 180, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.widget_2 = Plot(Nonlinear_regression_Form)
        self.widget_2.setGeometry(QtCore.QRect(30, 320, 791, 361))
        self.widget_2.setObjectName("widget_2")
        self.pushButton_4 = QtWidgets.QPushButton(Nonlinear_regression_Form)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 180, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(Nonlinear_regression_Form)
        self.label_2.setGeometry(QtCore.QRect(20, 280, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Nonlinear_regression_Form)
        self.label.setGeometry(QtCore.QRect(20, 150, 101, 16))
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(Nonlinear_regression_Form)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 220, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2 = QtWidgets.QPushButton(Nonlinear_regression_Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 180, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Nonlinear_regression_Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 20, 421, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Nonlinear_regression_Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 60, 421, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Nonlinear_regression_Form)
        self.label_4.setGeometry(QtCore.QRect(50, 20, 151, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Nonlinear_regression_Form)
        self.label_5.setGeometry(QtCore.QRect(50, 60, 141, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Nonlinear_regression_Form)
        self.lineEdit.setGeometry(QtCore.QRect(490, 280, 151, 21))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Nonlinear_regression_Form)
        self.label_3.setGeometry(QtCore.QRect(410, 280, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(Nonlinear_regression_Form)
        self.label_6.setGeometry(QtCore.QRect(660, 280, 72, 15))
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(Nonlinear_regression_Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(740, 280, 141, 21))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Nonlinear_regression_Form)
        QtCore.QMetaObject.connectSlotsByName(Nonlinear_regression_Form)

    def retranslateUi(self, Nonlinear_regression_Form):
        _translate = QtCore.QCoreApplication.translate
        Nonlinear_regression_Form.setWindowTitle(_translate("Nonlinear_regression_Form", "非线性回归"))
        self.pushButton_7.setText(_translate("Nonlinear_regression_Form", "指数曲线2"))
        self.pushButton_6.setText(_translate("Nonlinear_regression_Form", "S形曲线"))
        self.pushButton_3.setText(_translate("Nonlinear_regression_Form", "幂函数"))
        self.pushButton_4.setText(_translate("Nonlinear_regression_Form", "指数曲线1"))
        self.label_2.setText(_translate("Nonlinear_regression_Form", "回归曲线："))
        self.label.setText(_translate("Nonlinear_regression_Form", "选择拟合曲线"))
        self.pushButton_5.setText(_translate("Nonlinear_regression_Form", "对数曲线"))
        self.pushButton_2.setText(_translate("Nonlinear_regression_Form", "双曲线"))
        self.label_4.setText(_translate("Nonlinear_regression_Form", "x(用空格间隔样本点)"))
        self.label_5.setText(_translate("Nonlinear_regression_Form", "y(用空格间隔样本点)"))
        self.label_3.setText(_translate("Nonlinear_regression_Form", "参数b"))
        self.label_6.setText(_translate("Nonlinear_regression_Form", "参数a"))

from Plot import Plot

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Nonlinear_regression_Form = QtWidgets.QWidget()
    ui = Ui_Nonlinear_regression_Form()
    ui.setupUi(Nonlinear_regression_Form)
    Nonlinear_regression_Form.show()
    sys.exit(app.exec_())

