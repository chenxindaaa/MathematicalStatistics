# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import os
from PyQt5.QtGui import QIcon, QPixmap, QPainter
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication,  QInputDialog
from Fl_Sd_chi import Sd_chi_Form
from Ui_MainWindow import Ui_MainWindow
from Fl_Sd_t import  Sd_t_Form
from Fl_Sd_f import  Sd_f_Form
from Fl_Linear_regression import Form
from Fl_Sd_SingleNormal import Sd_SingleNormal_Form
from Fl_Nonlinear_regression import Nonlinear_regression_Form
from Fl_Sd_DoubleNormal import Sd_DoubleNormal_Form
from Fl_Simple_m_confidence_interval_ import  Simple_m_confidence_interval_Form
from Fl_double_confidence_interval import double_confidence_interval_Form
from Fl_dulixingjianyan import dulixingjianyan_Form
from Fl_FenbuhanshuNihe import FenbuhanshuNihe_Form
from FI_canshujiashejianyan_two import Supposetwo
from Fl_canshujiashejianyan import Suppose

class Fl_MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Fl_MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('./image/icon.png')) 
    
    def paintEvent(self,event):
        painter = QPainter(self)
        pixmap = QPixmap("./image/background.png")
        #绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(),pixmap)
    
    @pyqtSlot()
    def on_action_Sd_chi_triggered(self):
        """
        Slot documentation goes here.
        """
        self.Sd_chi=Sd_chi_Form()
        self.Sd_chi.show()
        
    @pyqtSlot()
    def on_action_Linear_regression_triggered(self):
        """
        Slot documentation goes here.
        """
        self.Linear_regression = Form()
        self.Linear_regression.show()
      
    @pyqtSlot()
    def on_action_Sd_t_triggered(self):
        """
        Slot documentation goes here.
        """
        self.Sd_t=Sd_t_Form()
        self.Sd_t.show()
        
    @pyqtSlot()
    def on_action_Sd_F_triggered(self):
        """
        Slot documentation goes here.
        """
        self.Sd_f=Sd_f_Form()
        self.Sd_f.show()
        
    @pyqtSlot()
    def on_action_Sd_SingleNormal_triggered(self):
        """
        Slot documentation goes here.
        """
        self.Sd_SingleNormal=Sd_SingleNormal_Form()
        self.Sd_SingleNormal.show()
        
    @pyqtSlot()    
    def on_action_Nonlinear_regression_triggered(self):
        """
        Slot documentation goes here.
        """
        self.Nonlinear_regression=Nonlinear_regression_Form()
        self.Nonlinear_regression.show()
        
    @pyqtSlot()
    def on_action_Sd_DoubleNormal_triggered(self):
        """
        Slot documentation goes here.
        """
        self.Sd_DoubleNormal=Sd_DoubleNormal_Form()
        self.Sd_DoubleNormal.show()
        
    @pyqtSlot()
    def on_Simple_m_confidence_interval_action_triggered(self):
        """
        Slot documentation goes here.
        """
        self.Simple_m_confidence_interval=Simple_m_confidence_interval_Form()
        value,  ok = self.do_btn15()
        if value == "自动生成样本":
            self.Simple_m_confidence_interval.lineEdit.hide()
            self.Simple_m_confidence_interval.pushButton_4.hide()
            self.Simple_m_confidence_interval.label_8.show()
            self.Simple_m_confidence_interval.spinBox.show()
        else:
            self.Simple_m_confidence_interval.lineEdit.show()
            self.Simple_m_confidence_interval.pushButton_4.show()
            self.Simple_m_confidence_interval.label_8.hide()
            self.Simple_m_confidence_interval.spinBox.hide()
        if ok:
            self.Simple_m_confidence_interval.show()
    
    def do_btn15(self): # 输入：选项
    #1为默认选中选项目，True/False 列表框是否可编辑。 
        items = ["自动生成样本", "手动导入样本"] 
        value, ok = QInputDialog.getItem(self, "模式选择", "请选择需要的模式：:", items, 1, False) 
        return value,  ok
        
    @pyqtSlot()
    def on_action_double_confidence_interval_triggered(self):
        """
        Slot documentation goes here.
        """
        self.double_confidence_interval = double_confidence_interval_Form()
        value,  ok = self.do_btn15()
        if value == "自动生成样本":
            self.double_confidence_interval.lineEdit.hide()
            self.double_confidence_interval.pushButton_7.hide()
            self.double_confidence_interval.label_6.show()
            self.double_confidence_interval.spinBox.show()
            self.double_confidence_interval.label_11.show()
            self.double_confidence_interval.spinBox_2.show()
        else:
            self.double_confidence_interval.lineEdit.show()
            self.double_confidence_interval.pushButton_7.show()
            self.double_confidence_interval.label_6.hide()
            self.double_confidence_interval.spinBox.hide()
            self.double_confidence_interval.label_11.hide()
            self.double_confidence_interval.spinBox_2.hide()
        if ok:
            self.double_confidence_interval.show()
    
    @pyqtSlot()
    def on_action_dulixingjianyan_triggered(self):
        """
        Slot documentation goes here.
        """
        self.dulixingjianyan = dulixingjianyan_Form()
        self.dulixingjianyan.show()

    @pyqtSlot()
    def on_action_18_triggered(self):
        """
        Slot documentation goes here.
        """
        self.FenbuhanshuNihe = FenbuhanshuNihe_Form()
        self.FenbuhanshuNihe.show()
        
    @pyqtSlot()
    def on_action_a_triggered(self):
        """
        Slot documentation goes here.
        """
        self.Suppose = Suppose()
        self.Suppose.show()
    
    @pyqtSlot()
    def on_action_16_triggered(self):
        """
        Slot documentation goes here.
        """
        self.Supposetwo=Supposetwo()
        self.Supposetwo.show()
        
    @pyqtSlot()
    def on_menu_5_aboutToShow(self):
        """
        Slot documentation goes here.
        """
        os.startfile(r'README.pdf')
    
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Fl_MainWindow()
    ui.show()
    sys.exit(app.exec_())        
