# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\94890\Desktop\Mathematical_Statistics\Myfiles\canshujiashejianyan.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Suppose(object):
    def setupUi(self, Suppose):
        Suppose.setObjectName("Suppose")
        Suppose.resize(1337, 883)
        self.centralwidget = QtWidgets.QWidget(Suppose)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 30, 331, 31))
        self.pushButton.setObjectName("pushButton")
        self.widget = Plot(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(460, 130, 811, 661))
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 30, 331, 501))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(6, 0, 6, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(1000000000)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout.addWidget(self.spinBox)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_7.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_7.setSizePolicy(sizePolicy)
        self.doubleSpinBox_7.setMaximum(1000000000.0)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.verticalLayout.addWidget(self.doubleSpinBox_7)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_4.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_4.setSizePolicy(sizePolicy)
        self.doubleSpinBox_4.setMaximum(10000000000.0)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.verticalLayout.addWidget(self.doubleSpinBox_4)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_5.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_5.setSizePolicy(sizePolicy)
        self.doubleSpinBox_5.setMaximum(1000000000.0)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.verticalLayout.addWidget(self.doubleSpinBox_5)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_6.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_6.setSizePolicy(sizePolicy)
        self.doubleSpinBox_6.setMaximum(1000000000.0)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.verticalLayout.addWidget(self.doubleSpinBox_6)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_8.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_8.setSizePolicy(sizePolicy)
        self.doubleSpinBox_8.setMaximum(1000000000.0)
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.verticalLayout.addWidget(self.doubleSpinBox_8)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy)
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.verticalLayout.addWidget(self.doubleSpinBox)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(60, 770, 331, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_6.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout.addWidget(self.lineEdit_6)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(60, 630, 331, 41))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_8.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setMaxLength(5)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_2.addWidget(self.lineEdit_8)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(60, 560, 331, 41))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_9.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setMaxLength(5)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_3.addWidget(self.lineEdit_9)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(920, 30, 331, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(60, 700, 331, 41))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_11.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy)
        self.lineEdit_11.setMaxLength(5)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_4.addWidget(self.lineEdit_11)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_10.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setMaxLength(5)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_4.addWidget(self.lineEdit_10)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 80, 331, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(920, 80, 331, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        Suppose.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Suppose)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1337, 26))
        self.menubar.setObjectName("menubar")
        Suppose.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Suppose)
        self.statusbar.setObjectName("statusbar")
        Suppose.setStatusBar(self.statusbar)

        self.retranslateUi(Suppose)
        QtCore.QMetaObject.connectSlotsByName(Suppose)

    def retranslateUi(self, Suppose):
        _translate = QtCore.QCoreApplication.translate
        Suppose.setWindowTitle(_translate("Suppose", "一个正态总体的参数假设检验"))
        self.pushButton.setText(_translate("Suppose", "均值检验（方差已知）"))
        self.label_8.setText(_translate("Suppose", "样本容量"))
        self.label_5.setText(_translate("Suppose", "方差"))
        self.label_6.setText(_translate("Suppose", "样本均值"))
        self.label_7.setText(_translate("Suppose", "样本方差"))
        self.label_4.setText(_translate("Suppose", "假设均值（上界）"))
        self.label_11.setText(_translate("Suppose", "假设方差（上界）"))
        self.label_2.setText(_translate("Suppose", "检验水平α"))
        self.label.setText(_translate("Suppose", "检验结果"))
        self.label_3.setText(_translate("Suppose", "统计量临界值"))
        self.label_9.setText(_translate("Suppose", "统计量观察值"))
        self.pushButton_2.setText(_translate("Suppose", "均值检验（方差未知）"))
        self.label_10.setText(_translate("Suppose", "统计量临界值"))
        self.pushButton_3.setText(_translate("Suppose", "方差检验（相等）"))
        self.pushButton_4.setText(_translate("Suppose", "方差检验(比较)"))

from Plot import Plot

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Suppose = QtWidgets.QMainWindow()
    ui = Ui_Suppose()
    ui.setupUi(Suppose)
    Suppose.show()
    sys.exit(app.exec_())

