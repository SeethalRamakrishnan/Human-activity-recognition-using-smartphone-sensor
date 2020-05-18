# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:lightcyan")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 90, 291, 31))
        self.lineEdit.setStyleSheet("background-color:white")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 100, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 20, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButtonTSNE = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonTSNE.setGeometry(QtCore.QRect(270, 222, 75, 31))
        self.pushButtonTSNE.setStyleSheet("background-color:#838faa")
        self.pushButtonTSNE.setObjectName("pushButtonTSNE")
        self.pushButtonHist = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHist.setGeometry(QtCore.QRect(460, 222, 75, 31))
        self.pushButtonHist.setStyleSheet("background-color:#838faa")
        self.pushButtonHist.setObjectName("pushButtonHist")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Human Activity Detection"))
        self.label.setText(_translate("MainWindow", "Dataset Path:"))
        self.label_2.setText(_translate("MainWindow", "Human Activity Detection"))
        self.pushButtonTSNE.setText(_translate("MainWindow", "TSNE"))
        self.pushButtonHist.setText(_translate("MainWindow", "Histogram"))
