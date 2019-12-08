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
        Sd_chi_Form.resize(903, 511)
        font = QtGui.QFont()
        font.setPointSize(12)
        Sd_chi_Form.setFont(font)
        self.label_4 = QtWidgets.QLabel(Sd_chi_Form)
        self.label_4.setGeometry(QtCore.QRect(350, 10, 131, 31))
        self.label_4.setObjectName("label_4")
        self.widget = Plot(Sd_chi_Form)
        self.widget.setGeometry(QtCore.QRect(360, 50, 511, 431))
        self.widget.setObjectName("widget")
        self.widget1 = QtWidgets.QWidget(Sd_chi_Form)
        self.widget1.setGeometry(QtCore.QRect(10, 190, 341, 144))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton_one = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_one.setChecked(True)
        self.radioButton_one.setObjectName("radioButton_one")
        self.horizontalLayout_4.addWidget(self.radioButton_one)
        self.radioButton_few = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_few.setObjectName("radioButton_few")
        self.horizontalLayout_4.addWidget(self.radioButton_few)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBox_chi_n = QtWidgets.QSpinBox(self.widget1)
        self.spinBox_chi_n.setObjectName("spinBox_chi_n")
        self.horizontalLayout.addWidget(self.spinBox_chi_n)
        self.pushButton_chi_plot = QtWidgets.QPushButton(self.widget1)
        self.pushButton_chi_plot.setObjectName("pushButton_chi_plot")
        self.horizontalLayout.addWidget(self.pushButton_chi_plot)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.doubleSpinBox_arfa = QtWidgets.QDoubleSpinBox(self.widget1)
        self.doubleSpinBox_arfa.setMinimum(0.01)
        self.doubleSpinBox_arfa.setMaximum(0.99)
        self.doubleSpinBox_arfa.setSingleStep(0.01)
        self.doubleSpinBox_arfa.setObjectName("doubleSpinBox_arfa")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_arfa)
        self.pushButton_quantile_plot = QtWidgets.QPushButton(self.widget1)
        self.pushButton_quantile_plot.setObjectName("pushButton_quantile_plot")
        self.horizontalLayout_2.addWidget(self.pushButton_quantile_plot)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_quantile = QtWidgets.QPushButton(self.widget1)
        self.pushButton_quantile.setObjectName("pushButton_quantile")
        self.horizontalLayout_3.addWidget(self.pushButton_quantile)
        self.lineEdit_quantile = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_quantile.setReadOnly(True)
        self.lineEdit_quantile.setObjectName("lineEdit_quantile")
        self.horizontalLayout_3.addWidget(self.lineEdit_quantile)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Sd_chi_Form)
        QtCore.QMetaObject.connectSlotsByName(Sd_chi_Form)

    def retranslateUi(self, Sd_chi_Form):
        _translate = QtCore.QCoreApplication.translate
        Sd_chi_Form.setWindowTitle(_translate("Sd_chi_Form", "卡方分布"))
        self.label_4.setText(_translate("Sd_chi_Form", "卡方分布："))
        self.radioButton_one.setText(_translate("Sd_chi_Form", "单个图像"))
        self.radioButton_few.setText(_translate("Sd_chi_Form", "多个图像"))
        self.label_2.setText(_translate("Sd_chi_Form", "输入n值："))
        self.pushButton_chi_plot.setText(_translate("Sd_chi_Form", "显示卡方分布图像"))
        self.label.setText(_translate("Sd_chi_Form", "输入α值："))
        self.pushButton_quantile_plot.setText(_translate("Sd_chi_Form", "显示分位点图像"))
        self.pushButton_quantile.setText(_translate("Sd_chi_Form", "显示分位点"))

from Plot import Plot

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sd_chi_Form = QtWidgets.QWidget()
    ui = Ui_Sd_chi_Form()
    ui.setupUi(Sd_chi_Form)
    Sd_chi_Form.show()
    sys.exit(app.exec_())

