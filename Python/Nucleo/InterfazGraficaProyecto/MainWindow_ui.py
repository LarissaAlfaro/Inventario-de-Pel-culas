# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        VentanaPrincipal.setObjectName("VentanaPrincipal")
        VentanaPrincipal.resize(358, 411)
        VentanaPrincipal.setStyleSheet("background-color: rgb(233, 152, 128)")
        self.centralwidget = QtWidgets.QWidget(VentanaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.About = QtWidgets.QPushButton(self.centralwidget)
        self.About.setGeometry(QtCore.QRect(230, 10, 111, 41))
        self.About.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(108, 79, 177);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.About.setAutoDefault(False)
        self.About.setObjectName("About")
        self.Add = QtWidgets.QPushButton(self.centralwidget)
        self.Add.setGeometry(QtCore.QRect(20, 240, 321, 41))
        self.Add.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(151, 208, 87);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.Add.setObjectName("Add")
        self.ViewAndEdit = QtWidgets.QPushButton(self.centralwidget)
        self.ViewAndEdit.setGeometry(QtCore.QRect(20, 290, 321, 41))
        self.ViewAndEdit.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(242, 234, 79);\n"
"color: rgb(220, 183, 104);\n"
"border-radius: 20px;")
        self.ViewAndEdit.setObjectName("ViewAndEdit")
        self.Display = QtWidgets.QPushButton(self.centralwidget)
        self.Display.setGeometry(QtCore.QRect(20, 340, 321, 41))
        self.Display.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(126, 189, 248);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.Display.setObjectName("Display")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 170, 211, 41))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(110, 70, 151, 91))
        self.lcdNumber.setObjectName("lcdNumber")
        VentanaPrincipal.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(VentanaPrincipal)
        self.statusbar.setObjectName("statusbar")
        VentanaPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(VentanaPrincipal)

    def retranslateUi(self, VentanaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        VentanaPrincipal.setWindowTitle(_translate("VentanaPrincipal", "Ventana Principal"))
        self.About.setText(_translate("VentanaPrincipal", "Acerca de"))
        self.Add.setText(_translate("VentanaPrincipal", "Agregar"))
        self.ViewAndEdit.setText(_translate("VentanaPrincipal", "Ver y Editar Listado"))
        self.Display.setText(_translate("VentanaPrincipal", "Visualizacion de Árbol"))
        self.label.setText(_translate("VentanaPrincipal", "<html><head/><body><p><span style=\" font-size:20pt;\">Películas en Total</span></p></body></html>"))
