# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\123.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets
import sys
import PySide2
import os

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

import urldata
import re
import webbrowser
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 130)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tburl = QtWidgets.QLineEdit(self.centralwidget)
        self.tburl.setGeometry(QtCore.QRect(80, 25, 350, 30))
        self.tburl.setObjectName("tburl")

        self.tbnum = QtWidgets.QLineEdit(self.centralwidget)
        self.tbnum.setGeometry(QtCore.QRect(140, 65, 290, 30))
        self.tbnum.setObjectName("tbnum")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 70, 18))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 120, 21))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.btrun = QtWidgets.QPushButton(self.centralwidget)
        self.btrun.setGeometry(QtCore.QRect(450, 30, 70, 70))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(12)
        self.btrun.setFont(font)
        self.btrun.setObjectName("btrun")
        self.btrun.clicked.connect(self.into)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 0, 380, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 355, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "網址:"))
        self.label_2.setText(_translate("MainWindow", "開始的集數:"))
        self.btrun.setText(_translate("MainWindow", "下載"))
        self.label_3.setText(_translate("MainWindow", "範例 : http://www.99kubo.tv/vod-read-id-XXXXX.html"))

    def into(self,MainWindow):
        url=self.tburl.text()
        print(url)
        data=urldata.urldatau(url)
        print(data)
        xfpall = data.find_all('a', {'href': re.compile('xfplay.html')})

        if self.tbnum.text() == "":
            urlsec="https://www.99kubo.tv" + xfpall[len(xfpall)-1]['href']

            datasec=urldata.urldatau(urlsec)

            xpdata = datasec.find(text=re.compile('dna'))
            regex= re.compile('dna.*?]')
            url=regex.findall(xpdata)
            webbrowser.open("xfplay://"+url[0])
        else:

            limit=int(self.tbnum.text())
            
            for a in range(len(xfpall)):
                if a >= limit-1:                 

                    urlsec="https://www.99kubo.tv" + xfpall[a]['href']
                    
                    datasec=urldata.urldatau(urlsec)

                    xpdata = datasec.find(text=re.compile('dna'))
                    regex= re.compile('dna.*?]')
                    url=regex.findall(xpdata)
                    webbrowser.open("xfplay://"+url[0])
                    time.sleep(2)

        



if __name__ == '__main__':  
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow) 
    MainWindow.show()
    sys.exit(app.exec_()) 
