# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\hehuibin\Desktop\MathematicalStatistics\Nonlinear_regression.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Nonlinear_regression_Form(object):
    def setupUi(self, Nonlinear_regression_Form):
        Nonlinear_regression_Form.setObjectName("Nonlinear_regression_Form")
        Nonlinear_regression_Form.resize(926, 703)
        self.widget_2 = Plot(Nonlinear_regression_Form)
        self.widget_2.setGeometry(QtCore.QRect(30, 320, 791, 361))
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QtWidgets.QLabel(Nonlinear_regression_Form)
        self.label_2.setGeometry(QtCore.QRect(20, 280, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Nonlinear_regression_Form)
        self.label.setGeometry(QtCore.QRect(20, 140, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Nonlinear_regression_Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 20, 421, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Nonlinear_regression_Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 60, 421, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Nonlinear_regression_Form)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Nonlinear_regression_Form)
        self.label_5.setGeometry(QtCore.QRect(30, 60, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Nonlinear_regression_Form)
        self.lineEdit.setGeometry(QtCore.QRect(80, 200, 111, 21))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Nonlinear_regression_Form)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(Nonlinear_regression_Form)
        self.label_6.setGeometry(QtCore.QRect(230, 200, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(Nonlinear_regression_Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 200, 111, 21))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.comboBox = QtWidgets.QComboBox(Nonlinear_regression_Form)
        self.comboBox.setGeometry(QtCore.QRect(170, 141, 141, 31))
        self.comboBox.setObjectName("comboBox")
        self.widget = QtWidgets.QWidget(Nonlinear_regression_Form)
        self.widget.setGeometry(QtCore.QRect(440, 130, 391, 161))
        self.widget.setObjectName("widget")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(70, 70, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 70, 111, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(70, 120, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_8.setGeometry(QtCore.QRect(180, 120, 111, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(70, 20, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Nonlinear_regression_Form)
        QtCore.QMetaObject.connectSlotsByName(Nonlinear_regression_Form)

    def retranslateUi(self, Nonlinear_regression_Form):
        _translate = QtCore.QCoreApplication.translate
        Nonlinear_regression_Form.setWindowTitle(_translate("Nonlinear_regression_Form", "非线性回归"))
        self.label_2.setText(_translate("Nonlinear_regression_Form", "回归曲线："))
        self.label.setText(_translate("Nonlinear_regression_Form", "选择拟合曲线"))
        self.label_4.setText(_translate("Nonlinear_regression_Form", "x(用空格间隔样本点)"))
        self.label_5.setText(_translate("Nonlinear_regression_Form", "y(用空格间隔样本点)"))
        self.label_3.setText(_translate("Nonlinear_regression_Form", "参数b"))
        self.label_6.setText(_translate("Nonlinear_regression_Form", "参数a"))
        self.label_8.setText(_translate("Nonlinear_regression_Form", "相关指数R"))
        self.label_10.setText(_translate("Nonlinear_regression_Form", "检验结果"))
        self.label_7.setText(_translate("Nonlinear_regression_Form", "默认显著性水准(0.01)"))

from Plot import Plot

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Nonlinear_regression_Form = QtWidgets.QWidget()
    ui = Ui_Nonlinear_regression_Form()
    ui.setupUi(Nonlinear_regression_Form)
    Nonlinear_regression_Form.show()
    sys.exit(app.exec_())

