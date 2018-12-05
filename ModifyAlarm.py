# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModifyAlarm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ModifyWindow(object):
    def setupUi(self, ModifyWindow):
        ModifyWindow.setObjectName("ModifyWindow")
        ModifyWindow.resize(731, 600)
        self.M_centralwidget = QtWidgets.QWidget(ModifyWindow)
        self.M_centralwidget.setObjectName("M_centralwidget")

        #Modify the time
        self.M_timeEdit = QtWidgets.QTimeEdit(self.M_centralwidget)
        self.M_timeEdit.setGeometry(QtCore.QRect(300, 10, 98, 32))
        self.M_timeEdit.setObjectName("M_timeEdit")

        #Modify the alarm     
        self.M_ModifyAlarm = QtWidgets.QPushButton(self.M_centralwidget)
        self.M_ModifyAlarm.setGeometry(QtCore.QRect(260, 200, 99, 32))
        self.M_ModifyAlarm.setObjectName("M_ModifyAlarm")

        #Modify the url
        self.M_URLTextBox = QtWidgets.QTextEdit(self.M_centralwidget)
        self.M_URLTextBox.setGeometry(QtCore.QRect(170, 100, 411, 41))
        self.M_URLTextBox.setObjectName("M_URLTextBox")
        
        self.M_URL = QtWidgets.QLabel(self.M_centralwidget)
        self.M_URL.setGeometry(QtCore.QRect(110, 100, 35, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.M_URL.setFont(font)
        self.M_URL.setObjectName("M_URL")

        #Modify the url        
        self.M_Repeat = QtWidgets.QLabel(self.M_centralwidget)
        self.M_Repeat.setGeometry(QtCore.QRect(150, 50, 50, 20))
        self.M_Repeat.setObjectName("M_Repeat")
        self.M_Monday = QtWidgets.QCheckBox(self.M_centralwidget)
        self.M_Monday.setGeometry(QtCore.QRect(220, 50, 50, 16))
        self.M_Monday.setObjectName("M_Monday")
        self.M_Tuesday = QtWidgets.QCheckBox(self.M_centralwidget)
        self.M_Tuesday.setGeometry(QtCore.QRect(290, 50, 50, 16))
        self.M_Tuesday.setObjectName("M_Tuesday")
        self.M_Wednesday = QtWidgets.QCheckBox(self.M_centralwidget)
        self.M_Wednesday.setGeometry(QtCore.QRect(360, 50, 50, 16))
        self.M_Wednesday.setObjectName("M_Wednesday")
        self.M_Thursday = QtWidgets.QCheckBox(self.M_centralwidget)
        self.M_Thursday.setGeometry(QtCore.QRect(430, 50, 50, 16))
        self.M_Thursday.setObjectName("M_Thursday")
        self.M_Friday = QtWidgets.QCheckBox(self.M_centralwidget)
        self.M_Friday.setGeometry(QtCore.QRect(500, 50, 50, 16))
        self.M_Friday.setObjectName("M_Friday")
        self.M_Saturday = QtWidgets.QCheckBox(self.M_centralwidget)
        self.M_Saturday.setGeometry(QtCore.QRect(570, 50, 50, 16))
        self.M_Saturday.setObjectName("M_Saturday")
        self.M_Sunday = QtWidgets.QCheckBox(self.M_centralwidget)
        self.M_Sunday.setGeometry(QtCore.QRect(640, 50, 50, 16))
        self.M_Sunday.setObjectName("M_Sunday")
        self.M_Close.clicked.connect(self.close_application)
        
        ModifyWindow.setCentralWidget(self.M_centralwidget)
        self.M_statusbar = QtWidgets.QStatusBar(ModifyWindow)
        self.M_statusbar.setObjectName("M_statusbar")
        ModifyWindow.setStatusBar(self.M_statusbar)
        self.menuBar = QtWidgets.QMenuBar(ModifyWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 731, 21))
        self.menuBar.setObjectName("menuBar")
        ModifyWindow.setMenuBar(self.menuBar)

        self.retranslateUi(ModifyWindow)
        QtCore.QMetaObject.connectSlotsByName(ModifyWindow)

    def retranslateUi(self, ModifyWindow):
        _translate = QtCore.QCoreApplication.translate
        ModifyWindow.setWindowTitle(_translate("ModifyWindow", "url alarm"))
        self.M_ModifyAlarm.setText(_translate("ModifyWindow", "Modify"))
        self.M_URL.setText(_translate("ModifyWindow", "URL"))
        self.M_Repeat.setText(_translate("ModifyWindow", "Repeat"))
        self.M_Monday.setText(_translate("ModifyWindow", "M"))
        self.M_Tuesday.setText(_translate("ModifyWindow", "Tu"))
        self.M_Wednesday.setText(_translate("ModifyWindow", "W"))
        self.M_Thursday.setText(_translate("ModifyWindow", "Th"))
        self.M_Friday.setText(_translate("ModifyWindow", "F"))
        self.M_Saturday.setText(_translate("ModifyWindow", "Sa"))
        self.M_Sunday.setText(_translate("ModifyWindow", "Su"))
        self.M_Close.setText(_translate("ModifyWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModifyWindow = QtWidgets.QMainWindow()
    ui = Ui_ModifyWindow()
    ui.setupUi(ModifyWindow)
    ModifyWindow.show()
    sys.exit(app.exec_())

