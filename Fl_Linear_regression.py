# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""
from PyQt5.QtGui import QIcon, QPixmap, QPainter 
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication,  QMessageBox
from Ui_Linear_regression import Ui_Linear_regression_Form

class Form(QWidget, Ui_Linear_regression_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Form, self).__init__(parent)
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
        try:
            x=list(map(float, self.lineEdit_5.text().strip().split(' ')))
            y=list(map(float, self.lineEdit_6.text().strip().split(' ')))
            parameter=self.widget.mpl.liner_fitting(x, y)
            self.lineEdit.setText(str(parameter[0]))
            self.lineEdit_2.setText(str(parameter[1]))
        except (IndexError,  ValueError):
            QMessageBox.information(self, "标题", "请输入数字并且保证x与y数量一致！(用一个空格间隔)", QMessageBox.Cancel)
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        self.widget.setVisible(True)
        try:
            x=list(map(float, self.lineEdit_5.text().strip().split(' ')))
            y=list(map(float, self.lineEdit_6.text().strip().split(' ')))
            parameter=self.widget.mpl.liner_fitting(x, y)
            draw_data = self.widget.mpl.calculate(x,parameter[0],parameter[1])
            self.widget.mpl.start_Linear_regression_plot(x, draw_data, y)
        except (IndexError,  ValueError):
            QMessageBox.information(self, "标题", "请输入数字并且保证x与y数量一致！(用一个空格间隔)", QMessageBox.Cancel)
            

        
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = Form()
    ui.show()
    sys.exit(app.exec_())
