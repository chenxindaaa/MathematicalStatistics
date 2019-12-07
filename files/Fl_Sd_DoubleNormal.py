# -*- coding: utf-8 -*-

"""
Module implementing Sd_DoubleNormal_Form.
"""
from PyQt5.QtGui import QIcon, QPixmap, QPainter 
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from Ui_Sd_DoubleNormal import Ui_Sd_DoubleNormal_Form

class Sd_DoubleNormal_Form(QWidget, Ui_Sd_DoubleNormal_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Sd_DoubleNormal_Form, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('./image/icon.png'))
    
    def paintEvent(self,event):
        painter = QPainter(self)
        pixmap = QPixmap("./image/background.png")
        #绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(),pixmap)
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        m1=self.spinBox_m1.value()
        n1=self.spinBox_n1.value()
        m2=self.spinBox_m2.value()
        n2=self.spinBox_n2.value()
        mu1=self.doubleSpinBox_mu1.value()
        sigma1=self.doubleSpinBox_sigma1.value()
        mu2=self.doubleSpinBox_mu2.value()
        sigma2=self.doubleSpinBox_sigma2.value()
        self.widget.setVisible(True)       
        if sigma1== 0 or sigma2 == 0:
            QMessageBox.information(self, "标题", "sigma不能为零", QMessageBox.Cancel)
        elif m1 != m2:
            QMessageBox.information(self, "标题", "抽样次数不同", QMessageBox.Cancel)
        else:
            self.widget.mpl.start_Double_Normal_plot1(m1, n1, m2, n2,  mu1, sigma1, mu2, sigma2)
        
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        m1=self.spinBox_m1.value()
        n1=self.spinBox_n1.value()
        m2=self.spinBox_m2.value()
        n2=self.spinBox_n2.value()
        mu1=self.doubleSpinBox_mu1.value()
        sigma1=self.doubleSpinBox_sigma1.value()
        mu2=self.doubleSpinBox_mu2.value()
        sigma2=self.doubleSpinBox_sigma2.value()
        self.widget.setVisible(True)      
        if sigma1== 0 or sigma2 == 0:
            QMessageBox.information(self, "标题", "sigma不能为零", QMessageBox.Cancel)
        elif m1 != m2:
            QMessageBox.information(self, "标题", "抽样次数不同", QMessageBox.Cancel)
        elif sigma1 != sigma2:
            QMessageBox.information(self, "标题", "sigma不同", QMessageBox.Cancel)
        else:
            self.widget.mpl.start_Double_Normal_plot2(m1, n1, m2, n2,  mu1, sigma1, mu2, sigma2) 
            
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        m1=self.spinBox_m1.value()
        n1=self.spinBox_n1.value()
        m2=self.spinBox_m2.value()
        n2=self.spinBox_n2.value()
        mu1=self.doubleSpinBox_mu1.value()
        sigma1=self.doubleSpinBox_sigma1.value()
        mu2=self.doubleSpinBox_mu2.value()
        sigma2=self.doubleSpinBox_sigma2.value()
        self.widget.setVisible(True)       
        if sigma1== 0 or sigma2 == 0:
            QMessageBox.information(self, "标题", "sigma不能为零", QMessageBox.Cancel)
        elif m1 != m2:
            QMessageBox.information(self, "标题", "抽样次数不同", QMessageBox.Cancel)
        else:
            self.widget.mpl.start_Double_Normal_plot3(m1, n1, m2, n2,  mu1, sigma1, mu2, sigma2)
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Sd_DoubleNormal_Form()
    ui.show()
    sys.exit(app.exec_()) 
