# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Area.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CalculateArea = QtWidgets.QPushButton(self.centralwidget)
        self.CalculateArea.setGeometry(QtCore.QRect(320, 400, 93, 28))
        self.CalculateArea.setObjectName("CalculateArea")
        self.SideA_2 = QtWidgets.QLabel(self.centralwidget)
        self.SideA_2.setGeometry(QtCore.QRect(50, 50, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SideA_2.setFont(font)
        self.SideA_2.setObjectName("SideA_2")
        self.SideA = QtWidgets.QTextEdit(self.centralwidget)
        self.SideA.setGeometry(QtCore.QRect(180, 50, 231, 41))
        self.SideA.setObjectName("SideA")
        self.SideB_2 = QtWidgets.QLabel(self.centralwidget)
        self.SideB_2.setGeometry(QtCore.QRect(50, 120, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SideB_2.setFont(font)
        self.SideB_2.setObjectName("SideB_2")
        self.SideB = QtWidgets.QTextEdit(self.centralwidget)
        self.SideB.setGeometry(QtCore.QRect(180, 140, 231, 41))
        self.SideB.setObjectName("SideB")
        self.Area = QtWidgets.QTextEdit(self.centralwidget)
        self.Area.setGeometry(QtCore.QRect(280, 250, 311, 87))
        self.Area.setObjectName("Area")
        self.Area_2 = QtWidgets.QLabel(self.centralwidget)
        self.Area_2.setGeometry(QtCore.QRect(140, 270, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Area_2.setFont(font)
        self.Area_2.setObjectName("Area_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.CalculateArea.clicked.connect(self.InputFeed)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CalculateArea.setText(_translate("MainWindow", "Calculate"))
        self.SideA_2.setText(_translate("MainWindow", "Side A"))
        self.SideB_2.setText(_translate("MainWindow", "Side B"))
        self.Area_2.setText(_translate("MainWindow", "Area"))
        

    def InputFeed(self):
        sideA = int(self.SideA.toPlainText())
        SideB = int(self.SideA.toPlainText())
        area = str((1/2)*sideA*SideB)       
        self.Area.setText(area)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

