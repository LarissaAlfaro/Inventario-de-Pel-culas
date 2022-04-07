# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Advertencia.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Advertencia(object):
    def setupUi(self, Advertencia):
        Advertencia.setObjectName("Advertencia")
        Advertencia.resize(399, 187)
        self.centralwidget = QtWidgets.QWidget(Advertencia)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 50, 291, 81))
        self.textBrowser.setStyleSheet("font: 75 11pt \"URW Bookman L\";")
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 161, 41))
        self.label.setStyleSheet("font: 75 11pt \"URW Bookman L\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 20, 89, 25))
        self.pushButton.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.pushButton.setObjectName("pushButton")
        Advertencia.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Advertencia)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 399, 22))
        self.menubar.setObjectName("menubar")
        Advertencia.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Advertencia)
        self.statusbar.setObjectName("statusbar")
        Advertencia.setStatusBar(self.statusbar)

        self.retranslateUi(Advertencia)
        QtCore.QMetaObject.connectSlotsByName(Advertencia)

    def retranslateUi(self, Advertencia):
        _translate = QtCore.QCoreApplication.translate
        Advertencia.setWindowTitle(_translate("Advertencia", "MainWindow"))
        self.textBrowser.setHtml(_translate("Advertencia", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'URW Bookman L\'; font-size:11pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:14pt; font-weight:400; color:#cc0000;\">Es obligatorio llenar los campos para añadir una pelicula</span></p></body></html>"))
        self.label.setText(_translate("Advertencia", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#cc0000;\">WARNING:</span></p></body></html>"))
        self.pushButton.setText(_translate("Advertencia", "Regresar"))
