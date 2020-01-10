# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""
from scipy.stats import f
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication , QMessageBox
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
        self.temp = []
        self.temp1 = []
        super(Sd_f_Form, self).__init__(parent)
        self.setupUi(self)
        self.widget.setVisible(False)
        self.setWindowIcon(QIcon('./image/icon.png'))
        self.a = 0.75
        self.b = 0.7
        self.radioButton_few.toggled.connect(self.clean)
        self.radioButton_one.toggled.connect(self.showitems)

        
    def clean(self):
        self.widget.mpl.axes.cla() 
        self.label_3.hide()
        self.doubleSpinBox_f_arfa.hide()
        self.pushButton_f_quantile_plot.hide()
        self.pushButton_f_quantile.hide()
        self.lineEdit_f_quantile.hide()
        
    def showitems(self):
        self.label_3.show()
        self.doubleSpinBox_f_arfa.show()
        self.pushButton_f_quantile_plot.show()
        self.pushButton_f_quantile.show()
        self.lineEdit_f_quantile.show()
    
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
        if f_n in self.temp and f_m in self.temp1 and self.radioButton_few.isChecked():
            QMessageBox.information(self, "标题", "此图已显示！", QMessageBox.Cancel)
        else:
            self.temp.append(f_n)
            self.temp1.append(f_m)
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
        self.widget.mpl.fill_f_plot(f_m, f_n, quantile, self.a,  self.b,  arfa)
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Sd_f_Form()
    ui.show()
    sys.exit(app.exec_())

