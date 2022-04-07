# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EmergenteAgregar.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_confirmAdd(object):
    def setupUi(self, confirmAdd):
        confirmAdd.setObjectName("confirmAdd")
        confirmAdd.resize(268, 152)
        confirmAdd.setStyleSheet("background-color:rgb(165, 233, 255)")
        self.label = QtWidgets.QLabel(confirmAdd)
        self.label.setGeometry(QtCore.QRect(0, 10, 271, 61))
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(confirmAdd)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 80, 61, 61))
        self.pushButton_3.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(255,0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"image: url(:/X/Cancelar.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(confirmAdd)
        self.pushButton.setGeometry(QtCore.QRect(160, 80, 61, 61))
        self.pushButton.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(0,255, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"image: url(:/Pleca/Comprobar.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(confirmAdd)
        QtCore.QMetaObject.connectSlotsByName(confirmAdd)

    def retranslateUi(self, confirmAdd):
        _translate = QtCore.QCoreApplication.translate
        confirmAdd.setWindowTitle(_translate("confirmAdd", "Confirmación"))
        self.label.setText(_translate("confirmAdd", "<html><head/><body><p><span style=\" font-size:16pt; color:#204a87;\">¿Desea cancelar la creación?</span></p></body></html>"))
from Nucleo.InterfazGraficaProyecto.Logos import Pleca_rc
from Nucleo.InterfazGraficaProyecto.Logos import X_rc
