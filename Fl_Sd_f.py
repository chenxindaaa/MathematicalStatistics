# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""
from scipy.stats import f
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication
from Ui_Sd_f import Ui_Sd_f_Form
from PyQt5.QtGui import QIcon, QPixmap, QPainter 

class Sd_f_Form(QWidget, Ui_Sd_f_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Sd_f_Form, self).__init__(parent)
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
        f_m=self.doubleSpinBox_f_m.value()
        f_n=self.doubleSpinBox_f_n.value()
        self.widget.setVisible(True)   
        if self.radioButton_one.isChecked():
            self.widget.mpl.axes.cla()     
        self.widget.mpl. start_f_plot(f_m, f_n)
        
    @pyqtSlot()
    def on_pushButton_f_quantile_clicked(self):
        """
        Slot documentation goes here.
        """ 
        f_n=self.doubleSpinBox_f_n.value()
        f_m=self.doubleSpinBox_f_m.value()
        arfa=self.doubleSpinBox_f_arfa.value()
        quantile=f.isf(arfa, f_m, f_n)
        self.lineEdit_f_quantile.setText('%.3f' % quantile)
        
    @pyqtSlot()
    def on_pushButton_f_quantile_plot_clicked(self):
        """
        Slot documentation goes here.
        """ 
        f_n=self.doubleSpinBox_f_n.value()
        f_m=self.doubleSpinBox_f_m.value()
        arfa=self.doubleSpinBox_f_arfa.value()
        quantile=f.isf(arfa, f_m, f_n)
        if self.radioButton_one.isChecked():
            self.widget.mpl.axes.cla()
            self.widget.mpl. start_f_plot(f_m, f_n)
        self.widget.mpl.fill_f_plot(f_m, f_n, quantile)
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Sd_f_Form()
    ui.show()
    sys.exit(app.exec_())

