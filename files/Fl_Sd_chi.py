# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""
from scipy.stats import chi2
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget,QApplication,  QMessageBox
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
        self.a = 0.75
        self.b = 0.7
        self.temp = []
        self.radioButton_few.toggled.connect(self.clean)
        self.radioButton_one.toggled.connect(self.showitems)

        
    def clean(self):
        self.widget.mpl.axes.cla()     
        self.label.hide()
        self.doubleSpinBox_arfa.hide()
        self.pushButton_quantile_plot.hide()
        self.lineEdit_quantile.hide()
        self.pushButton_quantile.hide()
        
    def showitems(self):
        self.label.show()
        self.doubleSpinBox_arfa.show()
        self.pushButton_quantile_plot.show()
        self.lineEdit_quantile.show()
        self.pushButton_quantile.show()
    
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
        if chi_n in self.temp and self.radioButton_few.isChecked():
            QMessageBox.information(self, "标题", "此图已显示！", QMessageBox.Cancel)
        else:
            self.temp.append(chi_n)
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
        self.widget.mpl.fill_chi_plot(chi_n, quantile,  self.a,  self.b, arfa)
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Sd_chi_Form()
    ui.show()
    sys.exit(app.exec_())

