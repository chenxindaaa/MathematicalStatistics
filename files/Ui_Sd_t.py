# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\94890\Desktop\YTfiles\Myfiles\Myfiles\files\Sd_t.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sd_t_Form(object):
    def setupUi(self, Sd_t_Form):
        Sd_t_Form.setObjectName("Sd_t_Form")
        Sd_t_Form.resize(930, 511)
        font = QtGui.QFont()
        font.setPointSize(12)
        Sd_t_Form.setFont(font)
        self.label_4 = QtWidgets.QLabel(Sd_t_Form)
        self.label_4.setGeometry(QtCore.QRect(460, 10, 131, 31))
        self.label_4.setObjectName("label_4")
        self.widget = Plot(Sd_t_Form)
        self.widget.setGeometry(QtCore.QRect(460, 50, 431, 421))
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(Sd_t_Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 190, 439, 138))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_one = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_one.setChecked(True)
        self.radioButton_one.setObjectName("radioButton_one")
        self.horizontalLayout.addWidget(self.radioButton_one)
        self.radioButton_few = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_few.setAutoExclusive(True)
        self.radioButton_few.setObjectName("radioButton_few")
        self.horizontalLayout.addWidget(self.radioButton_few)
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setAutoExclusive(False)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox.setDecimals(0)
        self.doubleSpinBox.setMinimum(0.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 0, 2, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.doubleSpinBox_t_arfa = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_t_arfa.setMinimum(0.01)
        self.doubleSpinBox_t_arfa.setMaximum(0.99)
        self.doubleSpinBox_t_arfa.setSingleStep(0.01)
        self.doubleSpinBox_t_arfa.setObjectName("doubleSpinBox_t_arfa")
        self.gridLayout.addWidget(self.doubleSpinBox_t_arfa, 1, 1, 1, 3)
        self.pushButton_t_quantile_plot = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_t_quantile_plot.setObjectName("pushButton_t_quantile_plot")
        self.gridLayout.addWidget(self.pushButton_t_quantile_plot, 1, 4, 1, 1)
        self.pushButton_t_quantile = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_t_quantile.setObjectName("pushButton_t_quantile")
        self.gridLayout.addWidget(self.pushButton_t_quantile, 2, 0, 1, 3)
        self.lineEdit_t_quantile = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_t_quantile.setReadOnly(True)
        self.lineEdit_t_quantile.setObjectName("lineEdit_t_quantile")
        self.gridLayout.addWidget(self.lineEdit_t_quantile, 2, 3, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Sd_t_Form)
        QtCore.QMetaObject.connectSlotsByName(Sd_t_Form)

    def retranslateUi(self, Sd_t_Form):
        _translate = QtCore.QCoreApplication.translate
        Sd_t_Form.setWindowTitle(_translate("Sd_t_Form", "t分布"))
        self.label_4.setText(_translate("Sd_t_Form", "t分布图像："))
        self.radioButton_one.setText(_translate("Sd_t_Form", "单个图像"))
        self.radioButton_few.setText(_translate("Sd_t_Form", "多个图像"))
        self.radioButton.setText(_translate("Sd_t_Form", "是否与正态分布比较"))
        self.label_2.setText(_translate("Sd_t_Form", "输入n值："))
        self.pushButton.setText(_translate("Sd_t_Form", "显示t分布图像"))
        self.label_3.setText(_translate("Sd_t_Form", "输入α值"))
        self.pushButton_t_quantile_plot.setText(_translate("Sd_t_Form", "显示分位点图像"))
        self.pushButton_t_quantile.setText(_translate("Sd_t_Form", "显示分位点"))
from Plot import Plot


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sd_t_Form = QtWidgets.QWidget()
    ui = Ui_Sd_t_Form()
    ui.setupUi(Sd_t_Form)
    Sd_t_Form.show()
    sys.exit(app.exec_())
