# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""
import math
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
        self.widget.setVisible(True)
        
        self.comboBox.clear()  # 清空items
        self.comboBox.addItem('请选择')
        
        self.comboBox.addItem("双曲线")
        self.comboBox.addItem("幂函数")
        self.comboBox.addItem("指数曲线1")
        self.comboBox.addItem("指数曲线2")
        self.comboBox.addItem("对数曲线")
        self.comboBox.addItem("S型曲线")
        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        
    def selectionchange(self,i):
            if i==1:
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
                        y1.append(float(1/y[i]))
                        i+=1
                    parameter=self.widget_2.mpl.liner_fitting(x1, y1)
                    self.lineEdit.setText(str("{:.6f}".format(parameter[0])))
                    self.lineEdit_4.setText(str("{:.6f}".format(parameter[1])))
                    j=0
                    Y=[]
                    while j<size:
                        Y.append(float(1/(parameter[0]*x1[j]+parameter[1])))
                        j+=1
                    self.widget_2.mpl.start_Linear_regression_plot(x,Y,y )
                    
                    sum=0
                    Q=0
                    lyy=0
                    for i in range(0, size):
                        sum+=y[i]
                    y_=sum/size
                    for i in range(0, size):
                        Q+=(y[i]-Y[i])**2
                        lyy+=(y[i]-y_)**2
                    R2=(1-Q/lyy)
                    if R2<=0:
                        self.lineEdit_6.setText(str(0))
                        self.lineEdit_8.setText(str("不显著"))
                    else:
                        R=R2**0.5
                        self.lineEdit_6.setText(str("{:.4f}".format(R)))
                        if R>=0.99:
                            self.lineEdit_8.setText(str("显著"))
                except (IndexError,  ValueError):
                    QMessageBox.information(self, "标题", "请正确输入数据样本", QMessageBox.Cancel)
                
                
                    
                    
            elif i==2:
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
                    self.lineEdit.setText(str("{:.6f}".format(parameter[0])))
                    self.lineEdit_4.setText(str("{:.6f}".format(math.exp(parameter[1]))))
                    j=0
                    Y=[]
                    while j<size:
                        Y.append(float(math.exp(parameter[0]*x1[j]+parameter[1])))
                        j+=1
                    self.widget_2.mpl.start_Linear_regression_plot(x,Y,y )
                    
                    sum=0
                    Q=0
                    lyy=0
                    for i in range(0, size):
                        sum+=y[i]
                    y_=sum/size
                    for i in range(0, size):
                        Q+=(y[i]-Y[i])**2
                        lyy+=(y[i]-y_)**2
                    R2=(1-Q/lyy)
                    if R2<=0:
                        self.lineEdit_6.setText(str(0))
                        self.lineEdit_8.setText(str("不显著"))
                    else:
                        R=R2**0.5
                        self.lineEdit_6.setText(str("{:.4f}".format(R)))
                        if R>=0.99:
                            self.lineEdit_8.setText(str("显著"))
                            
                except (IndexError,  ValueError):
                    QMessageBox.information(self, "标题", "请正确输入数据样本", QMessageBox.Cancel)
            
                
            elif i==3:
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
                    self.lineEdit.setText(str("{:.6f}".format(parameter[0])))
                    self.lineEdit_4.setText(str("{:.6f}".format(math.exp(parameter[1]))))
                    j=0
                    Y=[]
                    while j<size:
                        Y.append(float(math.exp(parameter[0]*x[j]+parameter[1])))
                        j+=1
                    self.widget_2.mpl.start_Linear_regression_plot(x,Y,y )
                    sum=0
                    Q=0
                    lyy=0
                    for i in range(0, size):
                        sum+=y[i]
                    y_=sum/size
                    for i in range(0, size):
                        Q+=(y[i]-Y[i])**2
                        lyy+=(y[i]-y_)**2
                    R2=(1-Q/lyy)
                    if R2<=0:
                        self.lineEdit_6.setText(str(0))
                        self.lineEdit_8.setText(str("不显著"))
                    else:
                        R=R2**0.5
                        self.lineEdit_6.setText(str("{:.4f}".format(R)))
                        if R>=0.99:
                            self.lineEdit_8.setText(str("显著"))
                    
                except (IndexError,  ValueError):
                    QMessageBox.information(self, "标题", "请正确输入数据样本", QMessageBox.Cancel)
            
            elif i==4:
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
                    self.lineEdit.setText(str("{:.6f}".format(parameter[0])))
                    self.lineEdit_4.setText(str("{:.6f}".format(math.exp(parameter[1]))))
                    j=0
                    Y=[]
                    while j<size:
                        Y.append(float(math.exp(parameter[0]*x1[j]+parameter[1])))
                        j+=1
                    self.widget_2.mpl.start_Linear_regression_plot(x,Y,y )
                    
                    sum=0
                    Q=0
                    lyy=0
                    for i in range(0, size):
                        sum+=y[i]
                    y_=sum/size
                    for i in range(0, size):
                        Q+=(y[i]-Y[i])**2
                        lyy+=(y[i]-y_)**2
                    R2=(1-Q/lyy)
                    if R2<=0:
                        self.lineEdit_6.setText(str(0))
                        self.lineEdit_8.setText(str("不显著"))
                    else:
                        R=R2**0.5
                        self.lineEdit_6.setText(str("{:.4f}".format(R)))
                        if R>=0.99:
                            self.lineEdit_8.setText(str("显著"))
                except (IndexError,  ValueError):
                    QMessageBox.information(self, "标题", "请正确输入数据样本", QMessageBox.Cancel)
            
                
            elif i==5:
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
                    self.lineEdit.setText(str("{:.6f}".format(parameter[0])))
                    self.lineEdit_4.setText(str("{:.6f}".format(parameter[1])))
                    j=0
                    Y=[]
                    while j<size:
                        Y.append(float(parameter[0]*x1[j]+parameter[1]))
                        j+=1
                    self.widget_2.mpl.start_Linear_regression_plot(x,Y,y )
                    
                    sum=0
                    Q=0
                    lyy=0
                    for i in range(0, size):
                        sum+=y[i]
                    y_=sum/size
                    for i in range(0, size):
                        Q+=(y[i]-Y[i])**2
                        lyy+=(y[i]-y_)**2
                    R2=(1-Q/lyy)
                    if R2<=0:
                        self.lineEdit_6.setText(str(0))
                        self.lineEdit_8.setText(str("不显著"))
                    else:
                        R=R2**0.5
                        self.lineEdit_6.setText(str("{:.4f}".format(R)))
                        if R>=0.99:
                            self.lineEdit_8.setText(str("显著"))
                    
                except (IndexError,  ValueError):
                    QMessageBox.information(self, "标题", "请正确输入数据样本", QMessageBox.Cancel)
            
        
            elif i==6:
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
                    self.lineEdit.setText(str("{:.6f}".format(parameter[0])))
                    self.lineEdit_4.setText(str("{:.6f}".format(parameter[1])))
                    j=0
                    Y=[]
                    while j<size:
                        Y.append(float(1/(parameter[0]*x1[j]+parameter[1])))
                        j+=1
                    self.widget_2.mpl.start_Linear_regression_plot(x,Y,y )
                    sum=0
                    Q=0
                    lyy=0
                    for i in range(0, size):
                        sum+=y[i]
                    y_=sum/size
                    for i in range(0, size):
                        Q+=(y[i]-Y[i])**2
                        lyy+=(y[i]-y_)**2
                    R2=(1-Q/lyy)
                    if R2<=0:
                        self.lineEdit_6.setText(str(0))
                        self.lineEdit_8.setText(str("不显著"))
                    else:
                        R=R2**0.5
                        self.lineEdit_6.setText(str("{:.4f}".format(R)))
                        if R>=0.99:
                            self.lineEdit_8.setText(str("显著"))
                except (IndexError,  ValueError):
                    QMessageBox.information(self, "标题", "请正确输入数据样本", QMessageBox.Cancel)
            
                
            else:
                pass
                
        
    def paintEvent(self,event):
        painter = QPainter(self)
        pixmap = QPixmap("./image/background.png")
        #绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(),pixmap) 
        
    
        
        
        
   
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = Nonlinear_regression_Form()
    ui.show()
    sys.exit(app.exec_())
