# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\94890\Desktop\YTfiles\Myfiles\Myfiles\files\dulixingjianyan.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dulixingjianyan_Form(object):
    def setupUi(self, dulixingjianyan_Form):
        dulixingjianyan_Form.setObjectName("dulixingjianyan_Form")
        dulixingjianyan_Form.resize(696, 504)
        self.label = QtWidgets.QLabel(dulixingjianyan_Form)
        self.label.setGeometry(QtCore.QRect(10, 40, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(dulixingjianyan_Form)
        self.textEdit.setGeometry(QtCore.QRect(170, 50, 251, 131))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(dulixingjianyan_Form)
        self.label_2.setGeometry(QtCore.QRect(30, 200, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(dulixingjianyan_Form)
        self.lineEdit.setGeometry(QtCore.QRect(170, 200, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(dulixingjianyan_Form)
        self.label_3.setGeometry(QtCore.QRect(30, 350, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(dulixingjianyan_Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 360, 111, 21))
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(dulixingjianyan_Form)
        self.label_5.setGeometry(QtCore.QRect(90, 400, 72, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(dulixingjianyan_Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 400, 113, 21))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(dulixingjianyan_Form)
        self.label_6.setGeometry(QtCore.QRect(390, 360, 72, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(dulixingjianyan_Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(460, 360, 113, 21))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_7 = QtWidgets.QLabel(dulixingjianyan_Form)
        self.label_7.setGeometry(QtCore.QRect(370, 400, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(dulixingjianyan_Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(460, 400, 113, 21))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(dulixingjianyan_Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 270, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(dulixingjianyan_Form)
        QtCore.QMetaObject.connectSlotsByName(dulixingjianyan_Form)

    def retranslateUi(self, dulixingjianyan_Form):
        _translate = QtCore.QCoreApplication.translate
        dulixingjianyan_Form.setWindowTitle(_translate("dulixingjianyan_Form", "独立性检验"))
        self.label.setText(_translate("dulixingjianyan_Form", "输入列联表矩阵"))
        self.label_2.setText(_translate("dulixingjianyan_Form", "显著性水平"))
        self.label_3.setText(_translate("dulixingjianyan_Form", "卡方值(统计量)"))
        self.label_5.setText(_translate("dulixingjianyan_Form", "临界值"))
        self.label_6.setText(_translate("dulixingjianyan_Form", "自由度"))
        self.label_7.setText(_translate("dulixingjianyan_Form", "检验结果"))
        self.pushButton.setText(_translate("dulixingjianyan_Form", "检验独立性"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dulixingjianyan_Form = QtWidgets.QWidget()
    ui = Ui_dulixingjianyan_Form()
    ui.setupUi(dulixingjianyan_Form)
    dulixingjianyan_Form.show()
    sys.exit(app.exec_())
