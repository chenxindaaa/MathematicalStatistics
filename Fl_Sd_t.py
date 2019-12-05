# -*- coding: utf-8 -*-

"""
Module implementing Sd_t_Form.
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication
from Ui_Sd_t import Ui_Sd_t_Form
from scipy import stats
from PyQt5.QtGui import QIcon, QPixmap, QPainter 

class Sd_t_Form(QWidget, Ui_Sd_t_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Sd_t_Form, self).__init__(parent)
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
        t_n=self.doubleSpinBox.value()
        self.widget.setVisible(True)  
        if self.radioButton_one.isChecked():
            self.widget.mpl.axes.cla()
        self.widget.mpl.start_t_plot(t_n)
        
    @pyqtSlot()
    def on_pushButton_t_quantile_clicked(self):
        """
        Slot documentation goes here.
        """ 
        t_n=self.doubleSpinBox.value()
        arfa=self.doubleSpinBox_t_arfa.value()
        quantile=stats.t.isf(arfa, t_n)
        self.lineEdit_t_quantile.setText('%.3f' % quantile)
        
    @pyqtSlot()
    def on_pushButton_t_quantile_plot_clicked(self):
        """
        Slot documentation goes here.
        """ 
        t_n=self.doubleSpinBox.value()
        arfa=self.doubleSpinBox_t_arfa.value()
        quantile=stats.t.isf(arfa, t_n)
        if self.radioButton_one.isChecked():
            self.widget.mpl.axes.cla()
            self.widget.mpl.start_t_plot(t_n)
        self.widget.mpl.fill_t_plot(t_n, quantile)
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Sd_t_Form()
    ui.show()
    sys.exit(app.exec_())
