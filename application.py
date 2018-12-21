# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'application.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Alarm
import os
from timer import *
from URLError import *
from ModifyAlarm import *
import timer


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        from timer import Ui_TimerWindow1
        import timer
        self.MainWindow = MainWindow
        
        #create an alarm instance
        self.Alarm = Alarm.Alarm()

        #main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #time
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(320, 10, 98, 32))
        self.timeEdit.setObjectName("timeEdit")

        #set the alarm
        self.SetAlarm = QtWidgets.QPushButton(self.centralwidget)
        self.SetAlarm.setGeometry(QtCore.QRect(320, 140, 99, 32))
        self.SetAlarm.setObjectName("SetAlarm")
        self.SetAlarm.clicked.connect(self.set_alarm)

        #set the alarm
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(180, 90, 411, 44))
        self.textEdit.setObjectName("URL_text")

        #url
        self.URL = QtWidgets.QLabel(self.centralwidget)
        self.URL.setGeometry(QtCore.QRect(110, 100, 31, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.URL.setFont(font)
        self.URL.setObjectName("URL")

        #repeat
        self.Repeat = QtWidgets.QLabel(self.centralwidget)
        self.Repeat.setGeometry(QtCore.QRect(130, 50, 50, 21))
        self.Repeat.setObjectName("Repeat")

        #to check if a day has been checked, call function ischecked
        self.Monday = QtWidgets.QCheckBox(self.centralwidget)
        self.Monday.setGeometry(QtCore.QRect(200, 50, 45, 20))
        self.Monday.setObjectName("Monday")

        self.Tuesday = QtWidgets.QCheckBox(self.centralwidget)
        self.Tuesday.setGeometry(QtCore.QRect(250, 50, 47, 20))
        self.Tuesday.setObjectName("Tuesday")

        self.Wednesday = QtWidgets.QCheckBox(self.centralwidget)
        self.Wednesday.setGeometry(QtCore.QRect(310, 50, 45, 20))
        self.Wednesday.setObjectName("Wednesday")

        self.Thursday = QtWidgets.QCheckBox(self.centralwidget)
        self.Thursday.setGeometry(QtCore.QRect(360, 50, 47, 20))
        self.Thursday.setObjectName("Thursday")

        self.Friday = QtWidgets.QCheckBox(self.centralwidget)
        self.Friday.setGeometry(QtCore.QRect(430, 50, 45, 20))
        self.Friday.setObjectName("Friday")

        self.Saturday = QtWidgets.QCheckBox(self.centralwidget)
        self.Saturday.setGeometry(QtCore.QRect(480, 50, 45, 20))
        self.Saturday.setObjectName("Saturday")

        self.Sunday = QtWidgets.QCheckBox(self.centralwidget)
        self.Sunday.setGeometry(QtCore.QRect(540, 50, 47, 20))
        self.Sunday.setObjectName("Sunday")

        #close button
        self.Close = QtWidgets.QPushButton(self.centralwidget)
        self.Close.setGeometry(QtCore.QRect(340, 510, 80, 31))
        self.Close.setObjectName("Close")
        self.Close.clicked.connect(self.close_application)

        #show the alarms

        self.Alarms = QtWidgets.QTableWidget(self.centralwidget)
        self.Alarms.setGeometry(QtCore.QRect(170, 180, 431, 321))
        self.Alarms.setObjectName("Alarms")
        self.Alarms.setColumnCount(2)
        self.Alarms.setColumnWidth(0, 100)
        self.Alarms.setColumnWidth(1, 331)
        self.Alarms.setHorizontalHeaderItem(0,QtWidgets.QTableWidgetItem("Time"))
        self.Alarms.setHorizontalHeaderItem(1,QtWidgets.QTableWidgetItem("URL"))

        #self.alarms.insertrow(self.alarms.currentrow() + 1) #insert new rows
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.Alarms)
        self.Alarms.doubleClicked.connect(self.modify_alarm) #return the clicked one


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #the menu bar is where the file, help buttons are
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 731, 17))
        self.menuBar.setObjectName("menuBar")
        
        #Attach Timer to something
        self.menuAlarm = QtWidgets.QMenu(self.menuBar)
        self.menuAlarm.setObjectName("menuAlarm")
        self.menuAlarm.setStatusTip('Timer')
        self.menuAlarm.triggered.connect(self.timer_function)

        MainWindow.setMenuBar(self.menuBar)
        self.actionTimer = QtWidgets.QAction(MainWindow)
        self.actionTimer.setObjectName("actionTimer")        
        self.menuAlarm.addAction(self.actionTimer)
        self.menuBar.addAction(self.menuAlarm.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "url alarm"))
        self.SetAlarm.setText(_translate("MainWindow", "set alarm"))
        self.URL.setText(_translate("MainWindow", "URL"))
        self.Repeat.setText(_translate("MainWindow", "Repeat"))
        self.Monday.setText(_translate("MainWindow", "M"))
        self.Tuesday.setText(_translate("MainWindow", "Tu"))
        self.Wednesday.setText(_translate("MainWindow", "W"))
        self.Thursday.setText(_translate("MainWindow", "Th"))
        self.Friday.setText(_translate("MainWindow", "F"))
        self.Saturday.setText(_translate("MainWindow", "Sa"))
        self.Sunday.setText(_translate("MainWindow", "Su"))
        self.Close.setText(_translate("MainWindow", "Close"))
        self.Alarms.setToolTip(_translate("MainWindow", "<html><head/><tr><th>Activate</th><th>Alarm</th><th>Other</th></html>"))
        self.menuAlarm.setTitle(_translate("MainWindow", "File"))
        self.actionTimer.setText(_translate("MainWindow", "Timer"))

    def close_application(self):
        print("Goodbye")
        sys.exit()

    def set_alarm(self):
        """Sets an alarm thorugh the alarm module"""
        """Keep track of what days have been checked"""

        days =[0, 0, 0, 0, 0, 0, 0]
        if self.Monday.isChecked():
            print("monday checked")
            days[0] = "mon"
        else:
            days[0] = "None"
        if self.Tuesday.isChecked():
            print("tue checked")
            days[1] = "tue"
        else:
            days[1] = "None"
        if self.Wednesday.isChecked():
            print("wed checked")
            days[2] = "wed"
        else:
            days[2] = "None"
        if self.Thursday.isChecked():
            print("thur checked")
            days[3] = "thur"
        else:
            days[3] = "None"
        if self.Friday.isChecked():
            print("fri checked")
            days[4] = "fri"
        else:
            days[4] = "None"
        if self.Saturday.isChecked():
            print("sat checked")
            days[5] = "sat"
        else:
            days[5] = "None"
        if self.Sunday.isChecked():
            print("sun checked")
            days[6] = "sun"
        else:
            days[6] = "None"
        print(days)

        url = self.textEdit.toPlainText()
        if (("http://" in url) or ("https://" in url)):
            """If it does exist, set the alarm and store it in the text screen"""
            self.Alarm.set_alarm(days, self.textEdit.toPlainText(), self.timeEdit.time().hour(),
                                                                    self.timeEdit.time().minute(), 0, 24)
            # make the row to store alarm info
            self.Alarms.insertRow(self.Alarms.currentRow() + 1)

            # display that info
            self.Alarms.setItem(self.Alarms.currentRow() + 1, self.Alarms.currentColumn() + 1, QtWidgets.QTableWidgetItem(str(self.timeEdit.time().hour()) + ":" + str(self.timeEdit.time().minute())))
            self.Alarms.setItem(self.Alarms.currentRow() + 1, self.Alarms.currentColumn() + 2, QtWidgets.QTableWidgetItem(str(self.textEdit.toPlainText())))
            self.textEdit.clear()
        else:
            """If the url does not exist, throw an error"""
            self.window=QtWidgets.QMainWindow()
            self.dp=Ui_ErrorWindoe()
            self.dp.setupUi(self.window)
            self.window.show()
            self.textEdit.clear()

    def timer_function(self):
        """Opens up a new window for timer and hides alarm"""
        self.Ui_TimerWindow1 = timer.Ui_TimerWindow1()
        self.window=QtWidgets.QMainWindow()
        self.dp=self.Ui_TimerWindow1
        self.dp.setup(self.window)
        self.window.show()
        self.MainWindow.hide()

    def modify_alarm(self):
        """Opens up a new window for modify"""
        self.window=QtWidgets.QMainWindow()
        self.dp=Ui_ModifyWindow()
        self.dp.setupUi(self.window)
        self.window.show()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

