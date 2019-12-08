# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\94890\Desktop\Mathematical_Statistics\Myfiles\Sd_SingleNormal.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Sd_SingleNormal_Form(object):
    def setupUi(self, Sd_SingleNormal_Form):
        Sd_SingleNormal_Form.setObjectName("Sd_SingleNormal_Form")
        Sd_SingleNormal_Form.resize(1123, 615)
        font = QtGui.QFont()
        font.setPointSize(12)
        Sd_SingleNormal_Form.setFont(font)
        self.widget = Plot(Sd_SingleNormal_Form)
        self.widget.setGeometry(QtCore.QRect(110, 180, 901, 391))
        self.widget.setObjectName("widget")
        self.widget1 = QtWidgets.QWidget(Sd_SingleNormal_Form)
        self.widget1.setGeometry(QtCore.QRect(180, 40, 745, 105))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.spinBox_n = QtWidgets.QSpinBox(self.widget1)
        self.spinBox_n.setMinimum(2)
        self.spinBox_n.setMaximum(999999999)
        self.spinBox_n.setObjectName("spinBox_n")
        self.horizontalLayout_2.addWidget(self.spinBox_n)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinBox_m = QtWidgets.QSpinBox(self.widget1)
        self.spinBox_m.setMinimum(1)
        self.spinBox_m.setMaximum(999999999)
        self.spinBox_m.setObjectName("spinBox_m")
        self.horizontalLayout_2.addWidget(self.spinBox_m)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.widget1)
        self.doubleSpinBox.setMinimum(-1e+31)
        self.doubleSpinBox.setMaximum(1e+28)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.widget1)
        self.doubleSpinBox_2.setMinimum(0.0)
        self.doubleSpinBox_2.setMaximum(1e+28)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(Sd_SingleNormal_Form)
        QtCore.QMetaObject.connectSlotsByName(Sd_SingleNormal_Form)

    def retranslateUi(self, Sd_SingleNormal_Form):
        _translate = QtCore.QCoreApplication.translate
        Sd_SingleNormal_Form.setWindowTitle(_translate("Sd_SingleNormal_Form", "单个正态总体抽样分布"))
        self.label.setText(_translate("Sd_SingleNormal_Form", "样本容量n"))
        self.label_2.setText(_translate("Sd_SingleNormal_Form", "抽样次数m"))
        self.label_3.setText(_translate("Sd_SingleNormal_Form", "μ"))
        self.label_4.setText(_translate("Sd_SingleNormal_Form", "σ"))
        self.pushButton.setText(_translate("Sd_SingleNormal_Form", "方差已知时，样本均值的分布"))
        self.pushButton_2.setText(_translate("Sd_SingleNormal_Form", "方差未知时，样本均值的分布"))
        self.pushButton_3.setText(_translate("Sd_SingleNormal_Form", "样本方差的抽样分布"))

from Plot import Plot

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sd_SingleNormal_Form = QtWidgets.QWidget()
    ui = Ui_Sd_SingleNormal_Form()
    ui.setupUi(Sd_SingleNormal_Form)
    Sd_SingleNormal_Form.show()
    sys.exit(app.exec_())

