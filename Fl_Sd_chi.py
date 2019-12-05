# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""
from scipy.stats import chi2
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget,QApplication
from Ui_Sd_chi import Ui_Sd_chi_Form
from PyQt5.QtGui import QIcon, QPixmap, QPainter 

class Sd_chi_Form(QWidget, Ui_Sd_chi_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Sd_chi_Form, self).__init__(parent)
        self.setupUi(self)
        self.widget.setVisible(False)
        self.setWindowIcon(QIcon('./image/icon.png')) 
    
    def paintEvent(self,event):
        painter = QPainter(self)
        pixmap = QPixmap("./image/background.png")
        #绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(),pixmap)
    
    @pyqtSlot()
    def on_pushButton_chi_plot_clicked(self):
        """
        Slot documentation goes here.
        """
        chi_n=self.spinBox_chi_n.value()
        self.widget.setVisible(True)   
        if self.radioButton_one.isChecked():
            self.widget.mpl.axes.cla()     
        self.widget.mpl.start_chi_plot(chi_n)

    @pyqtSlot()
    def on_pushButton_quantile_clicked(self):
        """
        Slot documentation goes here.
        """ 
        chi_n=self.spinBox_chi_n.value()
        arfa=self.doubleSpinBox_arfa.value()
        quantile=chi2.isf(arfa, chi_n)
        self.lineEdit_quantile.setText('%.3f' % quantile)
        
    @pyqtSlot()
    def on_pushButton_quantile_plot_clicked(self):
        """
        Slot documentation goes here.
        """ 
        chi_n=self.spinBox_chi_n.value()
        arfa=self.doubleSpinBox_arfa.value()
        quantile=chi2.isf(arfa, chi_n)
        if self.radioButton_one.isChecked():
            self.widget.mpl.axes.cla()
            self.widget.mpl.start_chi_plot(chi_n)
        self.widget.mpl.fill_chi_plot(chi_n, quantile)
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Sd_chi_Form()
    ui.show()
    sys.exit(app.exec_())

