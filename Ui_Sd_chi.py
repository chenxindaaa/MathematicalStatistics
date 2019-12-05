# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\94890\Desktop\Mathematical_Statistics\Myfiles\Sd_chi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Sd_chi_Form(object):
    def setupUi(self, Sd_chi_Form):
        Sd_chi_Form.setObjectName("Sd_chi_Form")
        Sd_chi_Form.resize(856, 497)
        self.label_4 = QtWidgets.QLabel(Sd_chi_Form)
        self.label_4.setGeometry(QtCore.QRect(350, 10, 131, 31))
        self.label_4.setObjectName("label_4")
        self.widget = Plot(Sd_chi_Form)
        self.widget.setGeometry(QtCore.QRect(350, 60, 451, 381))
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(Sd_chi_Form)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 190, 285, 106))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBox_chi_n = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_chi_n.setObjectName("spinBox_chi_n")
        self.horizontalLayout.addWidget(self.spinBox_chi_n)
        self.pushButton_chi_plot = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_chi_plot.setObjectName("pushButton_chi_plot")
        self.horizontalLayout.addWidget(self.pushButton_chi_plot)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.doubleSpinBox_arfa = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_arfa.setMinimum(0.01)
        self.doubleSpinBox_arfa.setMaximum(0.99)
        self.doubleSpinBox_arfa.setSingleStep(0.01)
        self.doubleSpinBox_arfa.setObjectName("doubleSpinBox_arfa")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_arfa)
        self.pushButton_quantile_plot = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_quantile_plot.setObjectName("pushButton_quantile_plot")
        self.horizontalLayout_2.addWidget(self.pushButton_quantile_plot)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_quantile = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_quantile.setObjectName("pushButton_quantile")
        self.horizontalLayout_3.addWidget(self.pushButton_quantile)
        self.lineEdit_quantile = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_quantile.setReadOnly(True)
        self.lineEdit_quantile.setObjectName("lineEdit_quantile")
        self.horizontalLayout_3.addWidget(self.lineEdit_quantile)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.layoutWidget_2 = QtWidgets.QWidget(Sd_chi_Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 140, 291, 21))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton_one = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.radioButton_one.setChecked(True)
        self.radioButton_one.setObjectName("radioButton_one")
        self.horizontalLayout_4.addWidget(self.radioButton_one)
        self.radioButton_few = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.radioButton_few.setObjectName("radioButton_few")
        self.horizontalLayout_4.addWidget(self.radioButton_few)

        self.retranslateUi(Sd_chi_Form)
        QtCore.QMetaObject.connectSlotsByName(Sd_chi_Form)

    def retranslateUi(self, Sd_chi_Form):
        _translate = QtCore.QCoreApplication.translate
        Sd_chi_Form.setWindowTitle(_translate("Sd_chi_Form", "卡方分布"))
        self.label_4.setText(_translate("Sd_chi_Form", "卡方分布："))
        self.label_2.setText(_translate("Sd_chi_Form", "输入n值："))
        self.pushButton_chi_plot.setText(_translate("Sd_chi_Form", "显示卡方分布图像"))
        self.label.setText(_translate("Sd_chi_Form", "输入α值："))
        self.pushButton_quantile_plot.setText(_translate("Sd_chi_Form", "显示分位点图像"))
        self.pushButton_quantile.setText(_translate("Sd_chi_Form", "显示分位点"))
        self.radioButton_one.setText(_translate("Sd_chi_Form", "单个图像"))
        self.radioButton_few.setText(_translate("Sd_chi_Form", "多个图像"))

from Plot import Plot

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sd_chi_Form = QtWidgets.QWidget()
    ui = Ui_Sd_chi_Form()
    ui.setupUi(Sd_chi_Form)
    Sd_chi_Form.show()
    sys.exit(app.exec_())

