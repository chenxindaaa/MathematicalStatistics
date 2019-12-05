# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""
from PyQt5.QtGui import QIcon, QPixmap, QPainter 
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from Ui_Sd_SingleNormal import Ui_Sd_SingleNormal_Form


class Sd_SingleNormal_Form(QWidget,Ui_Sd_SingleNormal_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Sd_SingleNormal_Form, self).__init__(parent)
        self.setupUi(self)
        self.widget.setVisible(False)
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
        mu=self.doubleSpinBox.value()
        sigma=self.doubleSpinBox_2.value()
        m=self.spinBox_m.value()
        n=self.spinBox_n.value()
        self.widget.setVisible(True)       
        if sigma != 0:
            self.widget.mpl.start_Single_Normal_plot1(m, n, mu, sigma)
        else:
            reply=QMessageBox.information(self, "标题", "sigma不能为零", QMessageBox.Cancel)
            print(reply)   
            
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        mu=self.doubleSpinBox.value()
        sigma=self.doubleSpinBox_2.value()
        m=self.spinBox_m.value()
        n=self.spinBox_n.value()
        self.widget.setVisible(True) 
        if sigma != 0:
            self.widget.mpl.start_Single_Normal_plot2(m, n, mu, sigma)
        else:
            reply=QMessageBox.information(self, "标题", "sigma不能为零", QMessageBox.Cancel)
            print(reply)      
    
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        mu=self.doubleSpinBox.value()
        sigma=self.doubleSpinBox_2.value()
        m=self.spinBox_m.value()
        n=self.spinBox_n.value()
        self.widget.setVisible(True)       
        if sigma != 0:
            self.widget.mpl.start_Single_Normal_plot3(m, n, mu, sigma)
        else:
            reply=QMessageBox.information(self, "标题", "sigma不能为零", QMessageBox.Cancel)
            print(reply)   
            
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Sd_SingleNormal_Form()
    ui.show()
    sys.exit(app.exec_())    
