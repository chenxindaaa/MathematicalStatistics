# -*- coding: utf-8 -*-

"""
Module implementing Form2.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QPainter 
from Ui_double_confidence_interval import Ui_double_confidence_interval_Form
from scipy.stats import t, norm, f


class double_confidence_interval_Form(QWidget, Ui_double_confidence_interval_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(double_confidence_interval_Form, self).__init__(parent)
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
        import numpy as np
        N1=int(self.spinBox.text())
        m1=float(self.doubleSpinBox_2.text())
        n1=float(self.doubleSpinBox_3.text())
        x = np.random.normal(m1, n1, N1)
        mean1, std1 = x.mean(), x.std(ddof=1)
        self.lineEdit_3.setText(str(round(mean1, 3)))
        self.lineEdit_4.setText(str(round(std1, 3)))
        N2=int(self.spinBox_2.text())
        m2=float(self.doubleSpinBox_4.text())
        n2=float(self.doubleSpinBox_5.text())
        y = np.random.normal(m2, n2, N2)
        mean2, std2 = y.mean(), y.std(ddof=1)
        self.lineEdit_5.setText(str(round(mean2, 3)))
        self.lineEdit_6.setText(str(round(std2, 3)))
        a=float(self.doubleSpinBox.text())
        z=norm.ppf(1-a/2,0,1)
        e=mean1-mean2-(z*((std1/N1+std2/N2)**0.5))
        f=mean1-mean2+(z*((std1/N1+std2/N2)**0.5))
        conf_intveral1=(round(e, 3), round(f, 3))
        self.lineEdit_21.setText(str(conf_intveral1))
        self.lineEdit_25.setText(str(''))
        self.widget.setVisible(True)
        self.widget.mpl.start_normal_plot(0,1)  
        self.widget.mpl.fill_normal_plot(a,0,1)
        # TODO: not implemented yet
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        import numpy as np
        from scipy import stats
        N1=int(self.spinBox.text())
        m1=float(self.doubleSpinBox_2.text())
        n1=float(self.doubleSpinBox_3.text())
        x = np.random.normal(m1, n1, N1)
        mean1, std1 = x.mean(), x.std(ddof=1)
        self.lineEdit_3.setText(str(round(mean1, 3)))
        self.lineEdit_4.setText(str(round(std1, 3)))
        N2=int(self.spinBox_2.text())
        m2=float(self.doubleSpinBox_4.text())
        n2=float(self.doubleSpinBox_5.text())
        y = np.random.normal(m2, n2, N2)
        mean2, std2 = y.mean(), y.std(ddof=1)
        self.lineEdit_5.setText(str(round(mean2, 3)))
        self.lineEdit_6.setText(str(round(std2, 3)))
        a=float(self.doubleSpinBox.text())
        p=t.ppf(1-a/2,N1+N2-2)
        s=((N1-1)*std1+(N2-1)*std2)/(N1+N2-2)
        e=mean1-mean2-p*s*((1/N1+1/N2)**0.5)
        f=mean1-mean2+p*s*((1/N1+1/N2)**0.5)
        conf_intveral1=(round(e, 3), round(f, 3))
        self.lineEdit_21.setText(str(conf_intveral1))
        self.lineEdit_25.setText(str(''))
        self.widget.setVisible(True)
        self.widget.mpl.start_t_plot1(N1+N2-2)  
        self.widget.mpl.fill_t_plot1(a,N1+N2-2)
        # TODO: not implemented yet
    
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        import numpy as np
        from scipy import stats
        N1=int(self.spinBox.text())
        m1=float(self.doubleSpinBox_2.text())
        n1=float(self.doubleSpinBox_3.text())
        x = np.random.normal(m1, n1, N1)
        mean1, std1 = x.mean(), x.std(ddof=1)
        self.lineEdit_3.setText(str(round(mean1, 3)))
        self.lineEdit_4.setText(str(round(std1, 3)))
        N2=int(self.spinBox_2.text())
        m2=float(self.doubleSpinBox_4.text())
        n2=float(self.doubleSpinBox_5.text())
        y = np.random.normal(m2, n2, N2)
        mean2, std2 = y.mean(), y.std(ddof=1)
        self.lineEdit_5.setText(str(round(mean2, 3)))
        self.lineEdit_6.setText(str(round(std2, 3)))
        a=float(self.doubleSpinBox.text())
        p=f.ppf(1-a/2,N1-1, N2-1)
        q=f.ppf(a/2,N1-1, N2-1)
        v=std1/(std2*q)
        w=std1/(std2*p)
        conf_intveral1=(round(v, 3), round(w, 3))
        self.lineEdit_25.setText(str(conf_intveral1))
        self.lineEdit_21.setText(str(''))
        self.widget.setVisible(True)
        self.widget.mpl.start_f_plot(N1-1, N2-1)  
        self.widget.mpl.fill_f_plot1(a,N1-1, N2-1)
        # TODO: not implemented yet
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = double_confidence_interval_Form()
    ui.show()
    sys.exit(app.exec_()) 
