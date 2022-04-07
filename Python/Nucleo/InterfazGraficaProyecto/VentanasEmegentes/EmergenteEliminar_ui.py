# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EmergenteEliminar.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_confirmRemove(object):
    def setupUi(self, confirmRemove):
        confirmRemove.setObjectName("confirmRemove")
        confirmRemove.resize(268, 151)
        confirmRemove.setStyleSheet("background-color:rgb(165, 233, 255);")
        self.label = QtWidgets.QLabel(confirmRemove)
        self.label.setGeometry(QtCore.QRect(0, 10, 271, 61))
        self.label.setStyleSheet("background-color:rgb(165, 233, 255);")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(confirmRemove)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 70, 61, 61))
        self.pushButton_3.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(255,0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"image: url(:/X/Cancelar.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(confirmRemove)
        self.pushButton.setGeometry(QtCore.QRect(160, 70, 61, 61))
        self.pushButton.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(0,255, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"image: url(:/Pleca/Comprobar.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(confirmRemove)
        QtCore.QMetaObject.connectSlotsByName(confirmRemove)

    def retranslateUi(self, confirmRemove):
        _translate = QtCore.QCoreApplication.translate
        confirmRemove.setWindowTitle(_translate("confirmRemove", "Confirmación"))
        self.label.setText(_translate("confirmRemove", "<html><head/><body><p><span style=\" font-size:16pt; color:#204a87;\">¿Desea eliminar la película?</span></p></body></html>"))
from Nucleo.InterfazGraficaProyecto.Logos import Pleca_rc
from Nucleo.InterfazGraficaProyecto.Logos import X_rc