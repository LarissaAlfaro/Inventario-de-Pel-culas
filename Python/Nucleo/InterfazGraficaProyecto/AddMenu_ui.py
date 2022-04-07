# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddMenu.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(694, 489)
        Dialog.setStyleSheet("background-color:rgb(165, 233, 255);")
        self.TxtName = QtWidgets.QLineEdit(Dialog)
        self.TxtName.setGeometry(QtCore.QRect(20, 10, 651, 51))
        self.TxtName.setStyleSheet("background-color:rgb(255,255,255);")
        self.TxtName.setInputMask("")
        self.TxtName.setText("")
        self.TxtName.setObjectName("TxtName")
        self.TxtDescription = QtWidgets.QTextEdit(Dialog)
        self.TxtDescription.setGeometry(QtCore.QRect(20, 130, 651, 151))
        self.TxtDescription.setStyleSheet("background-color:rgb(255,255,255);")
        self.TxtDescription.setObjectName("TxtDescription")
        self.TxtTime = QtWidgets.QLineEdit(Dialog)
        self.TxtTime.setGeometry(QtCore.QRect(20, 70, 651, 51))
        self.TxtTime.setStyleSheet("background-color:rgb(255,255,255);")
        self.TxtTime.setText("")
        self.TxtTime.setObjectName("TxtTime")
        self.TxtDirector = QtWidgets.QLineEdit(Dialog)
        self.TxtDirector.setGeometry(QtCore.QRect(20, 290, 651, 51))
        self.TxtDirector.setStyleSheet("background-color:rgb(255,255,255);")
        self.TxtDirector.setInputMask("")
        self.TxtDirector.setText("")
        self.TxtDirector.setObjectName("TxtDirector")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(20, 350, 651, 51))
        self.comboBox.setStyleSheet("background-color:rgb(255,255,255);")
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 420, 151, 51))
        self.pushButton_2.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(126, 189, 248);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 420, 101, 51))
        self.pushButton_3.setToolTip("")
        self.pushButton_3.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(225, 89, 123);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"image: url(:cesto/1f5d1.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Agregar Pelicula"))
        self.TxtName.setPlaceholderText(_translate("Dialog", "Nombre de la Película."))
        self.TxtDescription.setDocumentTitle(_translate("Dialog", "Nombr "))
        self.TxtDescription.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Nombr </title><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.TxtDescription.setPlaceholderText(_translate("Dialog", "Descripción de la Película."))
        self.TxtTime.setPlaceholderText(_translate("Dialog", "Duración (HH:MM:SS)"))
        self.TxtDirector.setPlaceholderText(_translate("Dialog", "Director de la Película."))
        self.comboBox.setCurrentText(_translate("Dialog", "[Seleccione el Género de la Película]"))
        self.comboBox.setItemText(0, _translate("Dialog", "[Seleccione el Género de la Película]"))
        self.comboBox.setItemText(1, _translate("Dialog", "Hechos Reales"))
        self.comboBox.setItemText(2, _translate("Dialog", "Bélicas"))
        self.comboBox.setItemText(3, _translate("Dialog", "Comedias Musicales"))
        self.comboBox.setItemText(4, _translate("Dialog", "Acción"))
        self.comboBox.setItemText(5, _translate("Dialog", "Artes Marciales"))
        self.comboBox.setItemText(6, _translate("Dialog", "Aventuras"))
        self.comboBox.setItemText(7, _translate("Dialog", "Ciencia Ficción"))
        self.comboBox.setItemText(8, _translate("Dialog", "Comedia"))
        self.comboBox.setItemText(9, _translate("Dialog", "Dibujos Animados"))
        self.comboBox.setItemText(10, _translate("Dialog", "Documental"))
        self.comboBox.setItemText(11, _translate("Dialog", "Espada y Hechicería"))
        self.comboBox.setItemText(12, _translate("Dialog", "Espionaje"))
        self.comboBox.setItemText(13, _translate("Dialog", "Horror"))
        self.comboBox.setItemText(14, _translate("Dialog", "Misterio"))
        self.comboBox.setItemText(15, _translate("Dialog", "Muertos Vivientes"))
        self.comboBox.setItemText(16, _translate("Dialog", "Propaganda"))
        self.comboBox.setItemText(17, _translate("Dialog", "Suspenso"))
        self.comboBox.setItemText(18, _translate("Dialog", "Terror"))
        self.comboBox.setItemText(19, _translate("Dialog", "Deportivas"))
        self.comboBox.setItemText(20, _translate("Dialog", "Dramáticas"))
        self.comboBox.setItemText(21, _translate("Dialog", "Fantásticas"))
        self.comboBox.setItemText(22, _translate("Dialog", "Infantiles"))
        self.comboBox.setItemText(23, _translate("Dialog", "Musicales"))
        self.comboBox.setItemText(24, _translate("Dialog", "Policíacas"))
        self.comboBox.setItemText(25, _translate("Dialog", "Psicológicas"))
        self.comboBox.setItemText(26, _translate("Dialog", "Románticas"))
        self.comboBox.setItemText(27, _translate("Dialog", "Animales"))
        self.comboBox.setItemText(28, _translate("Dialog", "Aviación"))
        self.comboBox.setItemText(29, _translate("Dialog", "Delincuencia"))
        self.comboBox.setItemText(30, _translate("Dialog", "Discapacitados"))
        self.comboBox.setItemText(31, _translate("Dialog", "Religión"))
        self.comboBox.setItemText(32, _translate("Dialog", "Política"))
        self.pushButton_2.setText(_translate("Dialog", "Agregar"))
from Nucleo.InterfazGraficaProyecto.Logos import cesto_rc
