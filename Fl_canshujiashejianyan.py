# -*- coding: utf-8 -*-

"""
Module implementing Suppose.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QPainter 
from Ui_canshujiashejianyan import Ui_Suppose
from scipy.stats import chi2, t, norm

class Suppose(QMainWindow, Ui_Suppose):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Suppose, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('./image/icon.png')) 
        
    def paintEvent(self,event):
        painter = QPainter(self)
        pixmap = QPixmap("./image/background.png")
        #绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(),pixmap)
    
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        N=int(self.spinBox.text())
        s=float(self.doubleSpinBox_7.text())#方差
        mean=float(self.doubleSpinBox_4.text())#样本均值
        m=float(self.doubleSpinBox_6.text())#假设均值
        a=float(self.doubleSpinBox.text())#检验水平
        if s !=0:
            u1=norm.ppf(1-a/2,0,1)#临界值
            U=(N**0.5)*(mean-m)/s#观察值
            self.lineEdit_9.setText(str(U))
            self.lineEdit_8.setText(str(u1))
            self.lineEdit_11.setText(str(''))
            self.lineEdit_10.setText(str(''))
            self.widget.setVisible(True)
            self.widget.mpl.start_normal_plot(0, 1)  
            self.widget.mpl.fill_normal_plot(a, 0, 1, U)
            if abs(U)>u1:
                self.lineEdit_6.setText(str('否定'))
            else:
                self.lineEdit_6.setText(str('不否定'))
        else:
            reply=QMessageBox.information(self, "提示","方差不能为0！")

    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        N=int(self.spinBox.text())
        s=float(self.doubleSpinBox_5.text())#样本方差
        mean=float(self.doubleSpinBox_4.text())#样本均值
        m=float(self.doubleSpinBox_6.text())#假设均值
        a=float(self.doubleSpinBox.text())#检验水平
        if s != 0:
            u2=t.ppf(1-a/2,N-1)#临界值
            T=((N-1)**0.5)*(mean-m)/s#观察值
            self.lineEdit_9.setText(str(T))
            self.lineEdit_8.setText(str(u2))
            self.lineEdit_11.setText(str(''))
            self.lineEdit_10.setText(str(''))
            self.widget.setVisible(True)
            self.widget.mpl.start_t_plot1(N-1)  
            self.widget.mpl.fill_t_plot1(a,N-1, T)
            if abs(T)>u2:
                self.lineEdit_6.setText(str('否定'))
            else:
                self.lineEdit_6.setText(str('不否定'))
        else:
            reply=QMessageBox.information(self, "提示","样本方差不能为0！")
        # TODO: not implemented yet

    
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        N=int(self.spinBox.text())
        s=float(self.doubleSpinBox_5.text())#样本方差
        m=float(self.doubleSpinBox_8.text())#假设方差
        a=float(self.doubleSpinBox.text())#检验水平
        if m != 0:
            u1=chi2.ppf(a/2,N-1)#临界值
            u2=chi2.ppf(1-a/2,N-1)#临界值
            X=(N*s)/m#观察值
            self.lineEdit_9.setText(str(X))
            self.lineEdit_8.setText(str(''))
            self.lineEdit_11.setText(str(u1))
            self.lineEdit_10.setText(str(u2))
            self.widget.setVisible(True)
            self.widget.mpl.start_chi2_plot(N-1)  
            self.widget.mpl.fill_chi2_plot(a,N-1, X)
            if abs(X)>u2 or abs(X)<u1:
                self.lineEdit_6.setText(str('否定'))
            else:
                self.lineEdit_6.setText(str('不否定'))
        else:
            reply=QMessageBox.information(self, "提示","假设方差不能为0！")
        # TODO: not implemented yet
        
    
    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        N=int(self.spinBox.text())
        s=float(self.doubleSpinBox_5.text())#样本方差
        m=float(self.doubleSpinBox_8.text())#假设方差
        a=float(self.doubleSpinBox.text())#检验水平
        if m != 0:
            u2=chi2.ppf(1-a,N-1)#临界值
            X=(N*s)/m#观察值
            self.lineEdit_9.setText(str(X))
            self.lineEdit_8.setText(str(u2))
            self.lineEdit_11.setText(str(''))
            self.lineEdit_10.setText(str(''))
            self.widget.setVisible(True)
            self.widget.mpl.start_chi2_plot(N-1)  
            self.widget.mpl.fill_chi2_plot1(1-a,N-1,  X)
            if abs(X)>=u2:
                self.lineEdit_6.setText(str('大于假设方差'))
            else:
                self.lineEdit_6.setText(str('不大于假设方差'))
        else:
            reply=QMessageBox.information(self, "提示","假设方差不能为0！")
        # TODO: not implemented yet
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Suppose()
    ui.show()
    sys.exit(app.exec_()) 
