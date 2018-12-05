# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'URLError.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ErrorWindoe(object):
    """This class creates the error window"""
    def setupUi(self, ErrorWindoe):
        ErrorWindoe.setObjectName("ErrorWindoe")
        ErrorWindoe.resize(400, 216)
        ErrorWindoe.setMaximumSize(QtCore.QSize(400, 16777215))
        
        self.E_centralwidget = QtWidgets.QWidget(ErrorWindoe)
        self.E_centralwidget.setObjectName("E_centralwidget")
                
        self.E_URL = QtWidgets.QLabel(self.E_centralwidget)
        self.E_URL.setGeometry(QtCore.QRect(150, 50, 155, 22))
        self.E_URL.setMaximumSize(QtCore.QSize(300, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.E_URL.setFont(font)
        self.E_URL.setObjectName("E_URL")
        
        ErrorWindoe.setCentralWidget(self.E_centralwidget)
        self.E_statusbar = QtWidgets.QStatusBar(ErrorWindoe)
        self.E_statusbar.setObjectName("E_statusbar")
        
        ErrorWindoe.setStatusBar(self.E_statusbar)
        self.E_menuBar = QtWidgets.QMenuBar(ErrorWindoe)
        self.E_menuBar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.E_menuBar.setObjectName("E_menuBar")
        ErrorWindoe.setMenuBar(self.E_menuBar)

        self.retranslateUi(ErrorWindoe)
        QtCore.QMetaObject.connectSlotsByName(ErrorWindoe)

    def retranslateUi(self, ErrorWindoe):
        _translate = QtCore.QCoreApplication.translate
        ErrorWindoe.setWindowTitle(_translate("ErrorWindoe", "url alarm"))
        self.E_URL.setText(_translate("ErrorWindoe", "Error: Invalid URL"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ErrorWindoe = QtWidgets.QMainWindow()
    ui = Ui_ErrorWindoe()
    ui.setupUi(ErrorWindoe)
    ErrorWindoe.show()
    sys.exit(app.exec_())

