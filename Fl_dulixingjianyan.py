# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QPixmap, QPainter
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QMessageBox
from Ui_dulixingjianyan import Ui_dulixingjianyan_Form
from scipy.stats import chi2_contingency
from scipy.stats import chi2

class dulixingjianyan_Form(QWidget, Ui_dulixingjianyan_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(dulixingjianyan_Form, self).__init__(parent)
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
        try: 
            A=[]
            Alpha=float(self.lineEdit.text())
            x=self.textEdit.toPlainText()
            X=list(x.split('\n'))
            h=len(X)
            for i in range(h):
                a=list(map(float, X[i].strip().split(' ')))
                A.append(a)
            parameter=self.chi2_independence(Alpha, A)
            self.lineEdit_2.setText(str("{:.2f}".format(parameter[0])))
            self.lineEdit_3.setText(str("{:.2f}".format(parameter[1])))
            self.lineEdit_4.setText(str(parameter[2]))
            self.lineEdit_5.setText(str(parameter[3]))
        except (ValueError):
            QMessageBox.information(self, "标题", "请输入数字！(用一个空格间隔)", QMessageBox.Cancel)
     
    def chi2_independence(self, alpha, data):
        g, p, dof, expctd = chi2_contingency(data)

        if dof == 0:
            print('自由度应该大于等于1')
        elif dof == 1:
            cv = chi2.isf(alpha * 0.5, dof)
        else:
            cv = chi2.isf(alpha * 0.5, dof-1)

        if g > cv:
            re = 0  # 表示拒绝原假设
        else:
            re = 1  # 表示接受原假设
            
        return g, cv, dof, re
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = dulixingjianyan_Form()
    ui.setupUi(Form)
    Form.setStyleSheet("#Form{border-image:url(C:/Users/94890/Desktop/Mathematical_Statistics/image/background.png);}")
    Form.show()
    sys.exit(app.exec_())
