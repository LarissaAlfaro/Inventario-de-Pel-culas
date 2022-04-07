# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExitoAdd.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Exito(object):
    def setupUi(self, Exito):
        Exito.setObjectName("Exito")
        Exito.resize(400, 119)
        Exito.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.pushButton = QtWidgets.QPushButton(Exito)
        self.pushButton.setGeometry(QtCore.QRect(290, 80, 89, 25))
        self.pushButton.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Exito)
        self.label.setGeometry(QtCore.QRect(50, 30, 291, 31))
        self.label.setStyleSheet("font: 75 11pt \"Ubuntu Mono\";")
        self.label.setObjectName("label")

        self.retranslateUi(Exito)
        QtCore.QMetaObject.connectSlotsByName(Exito)

    def retranslateUi(self, Exito):
        _translate = QtCore.QCoreApplication.translate
        Exito.setWindowTitle(_translate("Exito", "Dialog"))
        self.pushButton.setText(_translate("Exito", "Aceptar"))
        self.label.setText(_translate("Exito", "<html><head/><body><p><span style=\" font-size:14pt;\">Pelicula agregada con exito!</span></p></body></html>"))
