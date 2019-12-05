# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\94890\Desktop\Mathematical_Statistics\Myfiles\Sd_f.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Sd_f_Form(object):
    def setupUi(self, Sd_f_Form):
        Sd_f_Form.setObjectName("Sd_f_Form")
        Sd_f_Form.resize(856, 497)
        self.label_4 = QtWidgets.QLabel(Sd_f_Form)
        self.label_4.setGeometry(QtCore.QRect(340, 10, 131, 31))
        self.label_4.setObjectName("label_4")
        self.widget = Plot(Sd_f_Form)
        self.widget.setGeometry(QtCore.QRect(340, 50, 481, 411))
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(Sd_f_Form)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 180, 275, 129))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.doubleSpinBox_f_n = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_f_n.setObjectName("doubleSpinBox_f_n")
        self.gridLayout.addWidget(self.doubleSpinBox_f_n, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.doubleSpinBox_f_m = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_f_m.setObjectName("doubleSpinBox_f_m")
        self.gridLayout.addWidget(self.doubleSpinBox_f_m, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.doubleSpinBox_f_arfa = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_f_arfa.setMinimum(0.01)
        self.doubleSpinBox_f_arfa.setMaximum(0.99)
        self.doubleSpinBox_f_arfa.setSingleStep(0.01)
        self.doubleSpinBox_f_arfa.setObjectName("doubleSpinBox_f_arfa")
        self.horizontalLayout.addWidget(self.doubleSpinBox_f_arfa)
        self.pushButton_f_quantile_plot = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_f_quantile_plot.setObjectName("pushButton_f_quantile_plot")
        self.horizontalLayout.addWidget(self.pushButton_f_quantile_plot)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_f_quantile = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_f_quantile.setObjectName("pushButton_f_quantile")
        self.horizontalLayout_2.addWidget(self.pushButton_f_quantile)
        self.lineEdit_f_quantile = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_f_quantile.setReadOnly(True)
        self.lineEdit_f_quantile.setObjectName("lineEdit_f_quantile")
        self.horizontalLayout_2.addWidget(self.lineEdit_f_quantile)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(Sd_f_Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(50, 140, 291, 21))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_one = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.radioButton_one.setChecked(True)
        self.radioButton_one.setObjectName("radioButton_one")
        self.horizontalLayout_3.addWidget(self.radioButton_one)
        self.radioButton_few = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.radioButton_few.setObjectName("radioButton_few")
        self.horizontalLayout_3.addWidget(self.radioButton_few)

        self.retranslateUi(Sd_f_Form)
        QtCore.QMetaObject.connectSlotsByName(Sd_f_Form)

    def retranslateUi(self, Sd_f_Form):
        _translate = QtCore.QCoreApplication.translate
        Sd_f_Form.setWindowTitle(_translate("Sd_f_Form", "f分布"))
        self.label_4.setText(_translate("Sd_f_Form", "f分布图像："))
        self.label.setText(_translate("Sd_f_Form", "输入m值："))
        self.label_2.setText(_translate("Sd_f_Form", "输入n值："))
        self.pushButton.setText(_translate("Sd_f_Form", "显示f分布图像"))
        self.label_3.setText(_translate("Sd_f_Form", "输入α值"))
        self.pushButton_f_quantile_plot.setText(_translate("Sd_f_Form", "显示分位点图像"))
        self.pushButton_f_quantile.setText(_translate("Sd_f_Form", "显示分位点"))
        self.radioButton_one.setText(_translate("Sd_f_Form", "单个图像"))
        self.radioButton_few.setText(_translate("Sd_f_Form", "多个图像"))

from Plot import Plot

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sd_f_Form = QtWidgets.QWidget()
    ui = Ui_Sd_f_Form()
    ui.setupUi(Sd_f_Form)
    Sd_f_Form.show()
    sys.exit(app.exec_())

