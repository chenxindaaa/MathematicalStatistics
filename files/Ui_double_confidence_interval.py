# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\94890\Desktop\Mathematical_Statistics\Myfiles\files\double_confidence_interval.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_double_confidence_interval_Form(object):
    def setupUi(self, double_confidence_interval_Form):
        double_confidence_interval_Form.setObjectName("double_confidence_interval_Form")
        double_confidence_interval_Form.resize(1128, 683)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(double_confidence_interval_Form.sizePolicy().hasHeightForWidth())
        double_confidence_interval_Form.setSizePolicy(sizePolicy)
        self.pushButton = QtWidgets.QPushButton(double_confidence_interval_Form)
        self.pushButton.setGeometry(QtCore.QRect(780, 20, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.widget = Plot(double_confidence_interval_Form)
        self.widget.setGeometry(QtCore.QRect(500, 130, 591, 521))
        self.widget.setObjectName("widget")
        self.radioButton = QtWidgets.QRadioButton(double_confidence_interval_Form)
        self.radioButton.setGeometry(QtCore.QRect(500, 80, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_3 = QtWidgets.QRadioButton(double_confidence_interval_Form)
        self.radioButton_3.setGeometry(QtCore.QRect(960, 80, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_5 = QtWidgets.QRadioButton(double_confidence_interval_Form)
        self.radioButton_5.setGeometry(QtCore.QRect(730, 80, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.comboBox = QtWidgets.QComboBox(double_confidence_interval_Form)
        self.comboBox.setGeometry(QtCore.QRect(500, 20, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.comboBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.groupBox = QtWidgets.QGroupBox(double_confidence_interval_Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 50, 411, 351))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 271, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(290, 10, 121, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(11, 181, 47, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(11, 212, 80, 24))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_2.setGeometry(QtCore.QRect(118, 212, 171, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(999999999)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(11, 243, 100, 24))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(118, 243, 174, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_4.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_4.setSizePolicy(sizePolicy)
        self.doubleSpinBox_4.setMaximum(1e+29)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(11, 274, 100, 24))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_5.setGeometry(QtCore.QRect(118, 274, 174, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_5.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_5.setSizePolicy(sizePolicy)
        self.doubleSpinBox_5.setMaximum(1e+29)
        self.doubleSpinBox_5.setProperty("value", 1.0)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(11, 51, 47, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(11, 82, 80, 24))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(118, 82, 171, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(999999999)
        self.spinBox.setObjectName("spinBox")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(11, 113, 100, 24))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(118, 113, 174, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_2.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_2.setSizePolicy(sizePolicy)
        self.doubleSpinBox_2.setMaximum(1e+29)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(11, 144, 100, 24))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(118, 144, 174, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_3.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_3.setSizePolicy(sizePolicy)
        self.doubleSpinBox_3.setMaximum(1e+29)
        self.doubleSpinBox_3.setProperty("value", 1.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.widget1 = QtWidgets.QWidget(double_confidence_interval_Form)
        self.widget1.setGeometry(QtCore.QRect(30, 410, 411, 211))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_12 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 0, 2, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_5.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 0, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 1, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 1, 2, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_6.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 1, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy)
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setProperty("value", 0.05)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout.addWidget(self.doubleSpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_21.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_21.sizePolicy().hasHeightForWidth())
        self.lineEdit_21.setSizePolicy(sizePolicy)
        self.lineEdit_21.setMaxLength(20)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.verticalLayout.addWidget(self.lineEdit_21)
        self.label_10 = QtWidgets.QLabel(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_25.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_25.sizePolicy().hasHeightForWidth())
        self.lineEdit_25.setSizePolicy(sizePolicy)
        self.lineEdit_25.setMaxLength(20)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.verticalLayout.addWidget(self.lineEdit_25)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(double_confidence_interval_Form)
        QtCore.QMetaObject.connectSlotsByName(double_confidence_interval_Form)

    def retranslateUi(self, double_confidence_interval_Form):
        _translate = QtCore.QCoreApplication.translate
        double_confidence_interval_Form.setWindowTitle(_translate("double_confidence_interval_Form", "两个正态总体的区间估计"))
        self.pushButton.setText(_translate("double_confidence_interval_Form", "计算置信区间并显示图像"))
        self.radioButton.setText(_translate("double_confidence_interval_Form", "样本X频率直方图"))
        self.radioButton_3.setText(_translate("double_confidence_interval_Form", "样本分布图"))
        self.radioButton_5.setText(_translate("double_confidence_interval_Form", "样本Y频率直方图"))
        self.comboBox.setItemText(0, _translate("double_confidence_interval_Form", "均值差（方差已知）"))
        self.comboBox.setItemText(1, _translate("double_confidence_interval_Form", "均值差（方差未知）"))
        self.comboBox.setItemText(2, _translate("double_confidence_interval_Form", "方差比"))
        self.pushButton_7.setText(_translate("double_confidence_interval_Form", "导入样本"))
        self.label_8.setText(_translate("double_confidence_interval_Form", "样本Y"))
        self.label_11.setText(_translate("double_confidence_interval_Form", "样本容量"))
        self.label_3.setText(_translate("double_confidence_interval_Form", "请输入均值"))
        self.label_9.setText(_translate("double_confidence_interval_Form", "请输入方差"))
        self.label_2.setText(_translate("double_confidence_interval_Form", "样本X"))
        self.label_6.setText(_translate("double_confidence_interval_Form", "样本容量"))
        self.label_4.setText(_translate("double_confidence_interval_Form", "请输入均值"))
        self.label_5.setText(_translate("double_confidence_interval_Form", "请输入方差"))
        self.label_12.setText(_translate("double_confidence_interval_Form", "样本均值"))
        self.label_14.setText(_translate("double_confidence_interval_Form", "样本均值"))
        self.label_13.setText(_translate("double_confidence_interval_Form", "样本方差"))
        self.label_15.setText(_translate("double_confidence_interval_Form", "样本方差"))
        self.label.setText(_translate("double_confidence_interval_Form", "请输入显著性水平α "))
        self.label_7.setText(_translate("double_confidence_interval_Form", "均值差的置信区间（X-Y）"))
        self.label_10.setText(_translate("double_confidence_interval_Form", "方差比的置信区间（X/Y）"))

from Plot import Plot

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    double_confidence_interval_Form = QtWidgets.QWidget()
    ui = Ui_double_confidence_interval_Form()
    ui.setupUi(double_confidence_interval_Form)
    double_confidence_interval_Form.show()
    sys.exit(app.exec_())

