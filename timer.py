# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from application import *
import TimeCounter
import time
import webbrowser
from timer import *



class Ui_TimerWindow1(object):
    def setup(self, TimerWindow):
        self.TimerWindow = TimerWindow
        TimerWindow.setObjectName("TimerWindow")
        TimerWindow.resize(731, 600)
        self.T_centralwidget = QtWidgets.QWidget(TimerWindow)
        self.T_centralwidget.setObjectName("T_centralwidget")

        #The time edit
        self.T_timeEdit = QtWidgets.QTimeEdit(self.T_centralwidget)
        self.T_timeEdit.setGeometry(QtCore.QRect(320, 10, 98, 32))
        self.T_timeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.T_timeEdit.setObjectName("T_timeEdit")

        #Set the countdown
        self.SetTimer = QtWidgets.QPushButton(self.T_centralwidget)
        self.SetTimer.setGeometry(QtCore.QRect(320, 100, 99, 32))
        self.SetTimer.setObjectName("SetTimer")

        #Get the URL
        self.SetTimer.clicked.connect(self.set_timer)
        self.T_URLTextBox = QtWidgets.QTextEdit(self.T_centralwidget)
        self.T_URLTextBox.setGeometry(QtCore.QRect(170, 50, 411, 41))
        self.T_URLTextBox.setObjectName("T_URLTextBox")

        #URL label
        self.T_URL = QtWidgets.QLabel(self.T_centralwidget)
        self.T_URL.setGeometry(QtCore.QRect(110, 60, 31, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.T_URL.setFont(font)
        self.T_URL.setObjectName("T_URL")

        #Set the close button
        self.T_Close = QtWidgets.QPushButton(self.T_centralwidget)
        self.T_Close.setGeometry(QtCore.QRect(330, 140, 80, 31))
        self.T_Close.setObjectName("T_Close")

        #Set label to 0
        self.T_time = QtWidgets.QLabel(self.T_centralwidget)
        self.T_time.setGeometry(QtCore.QRect(340, 200, 170, 30))
        self.T_time.setMaximumSize(QtCore.QSize(300, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.T_time.setFont(font)
        self.T_time.setObjectName("T_time")
        
        self.T_Close.clicked.connect(self.close_application)
        TimerWindow.setCentralWidget(self.T_centralwidget)
        self.T_statusbar = QtWidgets.QStatusBar(TimerWindow)
        self.T_statusbar.setObjectName("T_statusbar")

        #The menu bar is where the file is, Alarm will be a function there as well
        TimerWindow.setStatusBar(self.T_statusbar)
        self.T_menuBar = QtWidgets.QMenuBar(TimerWindow)
        self.T_menuBar.setGeometry(QtCore.QRect(0, 0, 731, 21))
        self.T_menuBar.setObjectName("T_menuBar")

        #Attach the alarm to the menu bar
        self.T_menuTimer = QtWidgets.QMenu(self.T_menuBar)
        self.T_menuTimer.setObjectName("menuTimer")
        self.T_menuTimer.setStatusTip('Alarm')
        self.T_menuTimer.triggered.connect(self.alarm_function)

        TimerWindow.setMenuBar(self.T_menuBar)
        self.actionAlarm = QtWidgets.QAction(TimerWindow)
        self.actionAlarm.setObjectName("actionAlarm")        
        self.T_menuTimer.addAction(self.actionAlarm)
        self.T_menuBar.addAction(self.T_menuTimer.menuAction())

        self.retranslateUi(TimerWindow)
        QtCore.QMetaObject.connectSlotsByName(TimerWindow)

    def retranslateUi(self, TimerWindow):
        _translate = QtCore.QCoreApplication.translate
        TimerWindow.setWindowTitle(_translate("TimerWindow", "url alarm"))
        self.T_timeEdit.setDisplayFormat(_translate("TimerWindow", "hh:mm:ss"))
        self.SetTimer.setText(_translate("TimerWindow", "set timer"))
        self.T_URL.setText(_translate("TimerWindow", "URL"))
        self.T_Close.setText(_translate("TimerWindow", "Close"))
        self.T_time.setText(_translate("Timer Window", "off"))
        self.T_menuTimer.setTitle(_translate("MainWindow", "File"))
        self.actionAlarm.setText(_translate("MainWindow", "Alarm"))

    def close_application(self):
        """CLoses the window"""
        sys.exit()

    def set_timer(self):
        """This function begins the countdown"""
        #Calculates the amount of seconds in total
        self.T_time.setText("on")
        hour_in_sec = self.T_timeEdit.time().hour()*3600
        minute_in_sec = self.T_timeEdit.time().minute()*60
        total_sec = hour_in_sec + minute_in_sec + self.T_timeEdit.time().second()
        #Decrease the total until it reaches 0
        while total_sec > 0:
            time.sleep(1)
            total_sec -= 1
        #Then open the browser
        webbrowser.open(self.T_URLTextBox.toPlainText())
#        self.T_time.setText("off")
#        self.T_URLTextBoxt.clear()

    def alarm_function(self):
        """Opens up a new window for alarm and hides timer"""
        self.window=QtWidgets.QMainWindow()
        self.dp=Ui_MainWindow()
        self.dp.setupUi(self.window)
        self.window.show()
        self.TimerWindow.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TimerWindow = QtWidgets.QMainWindow()
    ui = Ui_TimerWindow1()
    ui.setup(TimerWindow)
    TimerWindow.show()
    sys.exit(app.exec_())

