# -*- coding: utf-8 -*-

"""
Module implementing Sd_t_Form.
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication,  QMessageBox
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
        self.temp = []
        super(Sd_t_Form, self).__init__(parent)
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
        self.doubleSpinBox_t_arfa.hide()
        self.pushButton_t_quantile_plot.hide()
        self.pushButton_t_quantile.hide()
        self.lineEdit_t_quantile.hide()
        self.radioButton.hide()
        
    def showitems(self):
        self.label_3.show()
        self.radioButton.show()
        self.doubleSpinBox_t_arfa.show()
        self.pushButton_t_quantile_plot.show()
        self.pushButton_t_quantile.show()
        self.lineEdit_t_quantile.show()
    
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
        if t_n in self.temp and self.radioButton_few.isChecked():
            QMessageBox.information(self, "标题", "此图已显示！", QMessageBox.Cancel)
        else:
            self.temp.append(t_n)
            self.widget.setVisible(True)  
            if self.radioButton_one.isChecked():
                self.widget.mpl.axes.cla()
            self.widget.mpl.start_t_plot(t_n,  self.radioButton.isChecked())
        
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
            self.widget.mpl.start_t_plot(t_n,  self.radioButton.isChecked())
        self.widget.mpl.fill_t_plot(t_n, quantile, self.a, self.b,  arfa)
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Sd_t_Form()
    ui.show()
    sys.exit(app.exec_())
