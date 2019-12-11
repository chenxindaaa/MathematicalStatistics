# -*- coding: utf-8 -*-

"""
Module implementing Supposetwo. 
"""

from PyQt5.QtCore import pyqtSlot     #修改注释
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QPainter
from Ui_canshujiashejianyan_two import Ui_Supposetwo
from scipy.stats import f,  t

class Supposetwo(QMainWindow, Ui_Supposetwo):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Supposetwo, self).__init__(parent)
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
        N1=int(self.spinBox.text())
        N2=int(self.spinBox_2.text())
        if N1 == N2:
            s1=float(self.doubleSpinBox_4.text())#样本均值a
            m1=float(self.doubleSpinBox_5.text())#样本方差a
            s2=float(self.doubleSpinBox_8.text())#样本均值b
            m2=float(self.doubleSpinBox_7.text())#样本方差b
            a=float(self.doubleSpinBox.text())#检验水平 
            z=s1-s2
            if m1+m2 != 0:
                S=(m1+m2)/N1
                u=((N1-1)**0.5)*z/S#观察值
                T=t.ppf(1-a/2, N1-1)#临界值
                self.lineEdit_8.setText(str(T))
                self.lineEdit_9.setText(str(u))
                self.lineEdit_10.setText(str(''))
                self.lineEdit_11.setText(str(''))
                self.widget.setVisible(True)
                self.widget.mpl.start_t_plot1(N1-1)  
                self.widget.mpl.fill_t_plot1(a,N1-1, u)
                if abs(u)>=T:
                    self.lineEdit_6.setText(str('否定'))
                else:
                    self.lineEdit_6.setText(str('不否定'))
            else:
                reply=QMessageBox.information(self, "提示","两个样本的方差之和为0！")
        else:
            reply=QMessageBox.information(self, "提示","样本容量不相等！")
        # TODO: not implemented yet
    
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        N1=int(self.spinBox.text())
        N2=int(self.spinBox_2.text())
        s1=float(self.doubleSpinBox_4.text())#样本均值a
        m1=float(self.doubleSpinBox_5.text())#样本方差a
        s2=float(self.doubleSpinBox_8.text())#样本均值b
        m2=float(self.doubleSpinBox_7.text())#样本方差b
        a=float(self.doubleSpinBox.text())#检验水平 
        if m2 != 0:
            u=((N2-1)*N1*m1)/((N1-1)*N2*m2)#观察值
            F1=f.ppf(1-a/2, N1-1, N2-1)#临界值
            F2=f.ppf(a/2, N1-1, N2-1)#临界值
            self.lineEdit_8.setText(str(''))
            self.lineEdit_9.setText(str(u))
            self.lineEdit_10.setText(str(F1))
            self.lineEdit_11.setText(str(F2))
            self.widget.setVisible(True)
            self.widget.mpl.start_f_plot(N1-1, N2-1)  
            self.widget.mpl.fill_f_plot1(a,N1-1, N2-1, u)
            if abs(u) > F1 or  abs(u) < F2:
                self.lineEdit_6.setText(str('否定'))
            else:
                self.lineEdit_6.setText(str('不否定'))
        else:
            reply=QMessageBox.information(self, "提示","样本B的方差为0！")
        # TODO: not implemented yet
    
    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        N1=int(self.spinBox.text())
        N2=int(self.spinBox_2.text())
        s1=float(self.doubleSpinBox_4.text())#样本均值a
        m1=float(self.doubleSpinBox_5.text())#样本方差a
        s2=float(self.doubleSpinBox_8.text())#样本均值b
        m2=float(self.doubleSpinBox_7.text())#样本方差b
        a=float(self.doubleSpinBox.text())#检验水平 
        if m2 != 0:
            u=((N2-1)*N1*m1)/((N1-1)*N2*m2)#观察值
            F1=f.ppf(1-a, N1-1, N2-1)#临界值
            self.lineEdit_8.setText(str(F1))
            self.lineEdit_9.setText(str(u))
            self.lineEdit_10.setText(str(''))
            self.lineEdit_11.setText(str(''))
            self.widget.setVisible(True)
            self.widget.mpl.start_f_plot(N1-1, N2-1)
            self.widget.mpl.fill_f_plot2(a,N1-1, N2-1,u)
            if abs(u) >= F1:
                self.lineEdit_6.setText(str('样本A的方差不大于样本B'))
            else:
                self.lineEdit_6.setText(str('样本A的方差大于样本B'))
        else:
            reply=QMessageBox.information(self, "提示","样本B的方差为0！")
        # TODO: not implemented yet
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        N1=int(self.spinBox.text())
        N2=int(self.spinBox_2.text())
        s1=float(self.doubleSpinBox_4.text())#样本均值a
        m1=float(self.doubleSpinBox_5.text())#样本方差a
        s2=float(self.doubleSpinBox_8.text())#样本均值b
        m2=float(self.doubleSpinBox_7.text())#样本方差b
        a=float(self.doubleSpinBox.text())#检验水平 
        if m1 != 0 or m2 != 0:
            z=s1-s2
            S=(N1*m1+N2*m2)**0.5
            N=N1+N2
            k=(N1*N2*(N-2))/N
            u=(k**0.5)*z/S#观察值
            T=t.ppf(1-a/2, N-2)#临界值
            self.lineEdit_8.setText(str(T))
            self.lineEdit_9.setText(str(u))
            self.lineEdit_10.setText(str(''))
            self.lineEdit_11.setText(str(''))
            self.widget.setVisible(True)
            self.widget.mpl.start_t_plot1(N-2)  
            self.widget.mpl.fill_t_plot1(a,N-2, u)
            if abs(u)>=T:
                self.lineEdit_6.setText(str('否定'))
            else:
                self.lineEdit_6.setText(str('不否定'))
        else:
            reply=QMessageBox.information(self, "提示","两个样本方差全为0！")
        # TODO: not implemented yet
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Supposetwo()
    ui.show()
    sys.exit(app.exec_()) 
