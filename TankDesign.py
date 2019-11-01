# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:40:33 2019
C:/Users/NaVnEeT/Anaconda3/Library/bin/pyuic5.bat -x TankCalcStacked.ui -o new.py
@author: NaVnEeT
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

Ui_MainWindow, QtBaseClass = uic.loadUiType('Area.ui')

class MyApp(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.CalculateArea.clicked.connect(self.InputFeed)

    def InputFeed(self):
        sideA = int(self.ui.SideA.toPlainText())
        SideB = int(self.ui.SideB.toPlainText())
        area = str((1/2)*sideA*SideB)       
        self.ui.Area.setText(area)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
