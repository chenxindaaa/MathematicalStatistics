# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""
import math
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication,  QMessageBox 
from Ui_Nonlinear_regression import Ui_Nonlinear_regression_Form
from PyQt5.QtGui import QIcon, QPixmap, QPainter

class Nonlinear_regression_Form(QWidget, Ui_Nonlinear_regression_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Nonlinear_regression_Form, self).__init__(parent)
        self.setupUi(self)
        self.widget_2.setVisible(False)
        self.setWindowIcon(QIcon('./image/icon.png')) 
      
    def paintEvent(self,event):
        painter = QPainter(self)
        pixmap = QPixmap("./image/background.png")
        #绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(),pixmap) 
     
    def on_pushButton_7_clicked(self):
        """
        Slot documentation goes here.
        """
        self.widget_2.setVisible(True)
        try:
            a=self.lineEdit_2.text()
            x=list(map(float, a.strip().split(' ')))
            b=self.lineEdit_3.text()
            y=list(map(float, b.strip().split(' ')))
            size=len(x)
            i=0
            x1=[]
            y1=[]
            while i<size:
                x1.append(float(1/x[i]))
                y1.append(float(math.log(y[i])))
                i+=1
            parameter=self.widget_2.mpl.liner_fitting(x1, y1)
            self.lineEdit.setText(str(parameter[0]))
            self.lineEdit_4.setText(str(math.exp(parameter[1])))
            j=0
            Y=[]
            while j<size:
                Y.append(float(math.exp(parameter[0]*x1[j]+parameter[1])))
                j+=1
            self.widget_2.mpl.start_Linear_regression_plot(x,Y,y )
        except (ValueError,  IndexError):
            QMessageBox.information(self, "标题", "请输入数字并且保证x与y数量一致！(用一个空格间隔)", QMessageBox.Cancel)
  
    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        """
        Slot documentation goes here.
        """
        self.widget_2.setVisible(True)
        try:
            a=self.lineEdit_2.text()
            x=list(map(float, a.strip().split(' ')))
            b=self.lineEdit_3.text()
            y=list(map(float, b.strip().split(' ')))
            size=len(x)
            i=0
            x1=[]
            y1=[]
            while i<size:
                x1.append(float(math.exp(-x[i])))
                y1.append(float(1/y[i]))
                i+=1
            parameter=self.widget_2.mpl.liner_fitting(x1, y1)
            self.lineEdit.setText(str(parameter[0]))
            self.lineEdit_4.setText(str(parameter[1]))
            j=0
            Y=[]
            while j<size:
                Y.append(float(1/(parameter[0]*x1[j]+parameter[1])))
                j+=1
            self.widget_2.mpl.start_Linear_regression_plot(x,Y,y )
        except (ValueError,  IndexError):
            QMessageBox.information(self, "标题", "请输入数字并且保证x与y数量一致！(用一个空格间隔)", QMessageBox.Cancel)
 
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        self.widget_2.setVisible(True)
        try:
            a=self.lineEdit_2.text()
            x=list(map(float, a.strip().split(' ')))
            b=self.lineEdit_3.text()
            y=list(map(float, b.strip().split(' ')))
            size=len(x)
            i=0
            x1=[]
            y1=[]
            while i<size:
                x1.append(float(math.log(x[i])))
                y1.append(float(math.log(y[i])))
                i+=1
            parameter=self.widget_2.mpl.liner_fitting(x1, y1)
            self.lineEdit.setText(str(parameter[0]))
            self.lineEdit_4.setText(str(math.exp(parameter[1])))
            j=0
            Y=[]
            while j<size:
                Y.append(float(math.exp(parameter[0]*x1[j]+parameter[1])))
                j+=1
            self.widget_2.mpl.start_Linear_regression_plot(x,Y,y )
        except (ValueError,  IndexError):
            QMessageBox.information(self, "标题", "请输入数字并且保证x与y数量一致！(用一个空格间隔)", QMessageBox.Cancel)   
    
    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        self.widget_2.setVisible(True)
        try:
            a=self.lineEdit_2.text()
            x=list(map(float, a.strip().split(' ')))
            b=self.lineEdit_3.text()
            y=list(map(float, b.strip().split(' ')))
            size=len(x)
            i=0
            y1=[]
            while i<size:
                y1.append(float(math.log(y[i])))
                i+=1
            parameter=self.widget_2.mpl.liner_fitting(x, y1)
            self.lineEdit.setText(str(parameter[0]))
            self.lineEdit_4.setText(str(math.exp(parameter[1])))
            j=0
            Y=[]
            while j<size:
                Y.append(float(math.exp(parameter[0]*x[j]+parameter[1])))
                j+=1
            self.widget_2.mpl.start_Linear_regression_plot(x,Y,y )
        except (ValueError,  IndexError):
            QMessageBox.information(self, "标题", "请输入数字并且保证x与y数量一致！(用一个空格间隔)", QMessageBox.Cancel)   
        
    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        """
        Slot documentation goes here.
        """
        self.widget_2.setVisible(True)
        try:
            a=self.lineEdit_2.text()
            x=list(map(float, a.strip().split(' ')))
            b=self.lineEdit_3.text()
            y=list(map(float, b.strip().split(' ')))
            size=len(x)
            i=0
            x1=[]
            while i<size:
                x1.append(float(math.log(x[i])))
                i+=1
            parameter=self.widget_2.mpl.liner_fitting(x1, y)
            self.lineEdit.setText(str(parameter[0]))
            self.lineEdit_4.setText(str(parameter[1]))
            j=0
            Y=[]
            while j<size:
                Y.append(float(parameter[0]*x1[j]+parameter[1]))
                j+=1
            self.widget_2.mpl.start_Linear_regression_plot(x,Y,y )
        except (ValueError,  IndexError):
            QMessageBox.information(self, "标题", "请输入数字并且保证x与y数量一致！(用一个空格间隔)", QMessageBox.Cancel)   
         
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            self.widget_2.setVisible(True)
            a=self.lineEdit_2.text()
            x=list(map(float, a.strip().split(' ')))
            b=self.lineEdit_3.text()
            y=list(map(float, b.strip().split(' ')))
            size=len(x)
            i=0
            x1=[]
            y1=[]
            while i<size:
                x1.append(float(1/x[i]))
                y1.append(float(1/y[i]))
                i+=1
            parameter=self.widget_2.mpl.liner_fitting(x1, y1)
            self.lineEdit.setText(str(parameter[0]))
            self.lineEdit_4.setText(str(parameter[1]))
            j=0
            Y=[]
            while j<size:
                Y.append(float(1/(parameter[0]*x1[j]+parameter[1])))
                j+=1
            self.widget_2.mpl.start_Linear_regression_plot(x,Y,y )
        except (ValueError,  IndexError):
            QMessageBox.information(self, "标题", "请输入数字并且保证x与y数量一致！(用一个空格间隔)", QMessageBox.Cancel)   

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = Nonlinear_regression_Form()
    ui.show()
    sys.exit(app.exec_())
