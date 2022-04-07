# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditMenu.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editMovie(object):
    def setupUi(self, editMovie):
        editMovie.setObjectName("editMovie")
        editMovie.resize(694, 600)
        editMovie.setStyleSheet("background-color:rgb(165, 233, 255);")
        self.TxtName = QtWidgets.QLineEdit(editMovie)
        self.TxtName.setGeometry(QtCore.QRect(10, 30, 651, 51))
        self.TxtName.setStyleSheet("background-color:rgb(255,255,255);")
        self.TxtName.setInputMask("")
        self.TxtName.setText("")
        self.TxtName.setObjectName("TxtName")
        self.TxtDescription = QtWidgets.QTextEdit(editMovie)
        self.TxtDescription.setGeometry(QtCore.QRect(10, 190, 651, 151))
        self.TxtDescription.setStyleSheet("background-color:rgb(255,255,255);")
        self.TxtDescription.setObjectName("TxtDescription")
        self.TxtTime = QtWidgets.QLineEdit(editMovie)
        self.TxtTime.setGeometry(QtCore.QRect(10, 110, 651, 51))
        self.TxtTime.setStyleSheet("background-color:rgb(255,255,255);")
        self.TxtTime.setText("")
        self.TxtTime.setObjectName("TxtTime")
        self.TxtDirector = QtWidgets.QLineEdit(editMovie)
        self.TxtDirector.setGeometry(QtCore.QRect(10, 370, 651, 51))
        self.TxtDirector.setStyleSheet("background-color:rgb(255,255,255);")
        self.TxtDirector.setInputMask("")
        self.TxtDirector.setText("")
        self.TxtDirector.setObjectName("TxtDirector")
        self.comboBox = QtWidgets.QComboBox(editMovie)
        self.comboBox.setGeometry(QtCore.QRect(10, 450, 651, 51))
        self.comboBox.setStyleSheet("background-color:rgb(255,255,255);")
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
        self.pushButton_2 = QtWidgets.QPushButton(editMovie)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 520, 171, 51))
        self.pushButton_2.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(126, 189, 248);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(editMovie)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(editMovie)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 161, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(editMovie)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 181, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(editMovie)
        self.label_4.setGeometry(QtCore.QRect(10, 350, 161, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(editMovie)
        self.label_5.setGeometry(QtCore.QRect(10, 430, 67, 17))
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(editMovie)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 520, 89, 51))
        self.pushButton_3.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(225, 89, 123);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"image: url(:/X/Cancelar.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(editMovie)
        QtCore.QMetaObject.connectSlotsByName(editMovie)

    def retranslateUi(self, editMovie):
        _translate = QtCore.QCoreApplication.translate
        editMovie.setWindowTitle(_translate("editMovie", "Editar Pelicula"))
        self.TxtDescription.setDocumentTitle(_translate("editMovie", "Nombr "))
        self.TxtDescription.setHtml(_translate("editMovie", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Nombr </title><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.comboBox.setItemText(0, _translate("editMovie", "[Seleccione el Género de la Película]"))
        self.comboBox.setItemText(1, _translate("editMovie", "Hechos Reales"))
        self.comboBox.setItemText(2, _translate("editMovie", "Bélicas"))
        self.comboBox.setItemText(3, _translate("editMovie", "Comedias Musicales"))
        self.comboBox.setItemText(4, _translate("editMovie", "Acción"))
        self.comboBox.setItemText(5, _translate("editMovie", "Artes Marciales"))
        self.comboBox.setItemText(6, _translate("editMovie", "Aventuras"))
        self.comboBox.setItemText(7, _translate("editMovie", "Ciencia Ficción"))
        self.comboBox.setItemText(8, _translate("editMovie", "Comedia"))
        self.comboBox.setItemText(9, _translate("editMovie", "Dibujos Animados"))
        self.comboBox.setItemText(10, _translate("editMovie", "Documental"))
        self.comboBox.setItemText(11, _translate("editMovie", "Espada y Hechicería"))
        self.comboBox.setItemText(12, _translate("editMovie", "Espionaje"))
        self.comboBox.setItemText(13, _translate("editMovie", "Horror"))
        self.comboBox.setItemText(14, _translate("editMovie", "Misterio"))
        self.comboBox.setItemText(15, _translate("editMovie", "Terror"))
        self.comboBox.setItemText(16, _translate("editMovie", "Deportivas"))
        self.comboBox.setItemText(17, _translate("editMovie", "Dramáticas"))
        self.comboBox.setItemText(18, _translate("editMovie", "Fantásticas"))
        self.comboBox.setItemText(19, _translate("editMovie", "Infantiles"))
        self.comboBox.setItemText(20, _translate("editMovie", "Musicales"))
        self.comboBox.setItemText(21, _translate("editMovie", "Policíacas"))
        self.comboBox.setItemText(22, _translate("editMovie", "Psicológicas"))
        self.comboBox.setItemText(23, _translate("editMovie", "Románticas"))
        self.comboBox.setItemText(24, _translate("editMovie", "Animales"))
        self.comboBox.setItemText(25, _translate("editMovie", "Aviación"))
        self.comboBox.setItemText(26, _translate("editMovie", "Delincuencia"))
        self.comboBox.setItemText(27, _translate("editMovie", "Discapacitados"))
        self.comboBox.setItemText(28, _translate("editMovie", "Religión"))
        self.comboBox.setItemText(29, _translate("editMovie", "Política"))
        self.pushButton_2.setText(_translate("editMovie", "Guardar Cambios"))
        self.label.setText(_translate("editMovie", "Nombre de la Película:"))
        self.label_2.setText(_translate("editMovie", "Duración (HH:MM:SS):"))
        self.label_3.setText(_translate("editMovie", "Descripción de la Película:"))
        self.label_4.setText(_translate("editMovie", "Director de la Película:"))
        self.label_5.setText(_translate("editMovie", "Género:"))
from Nucleo.InterfazGraficaProyecto.Logos import X_rc
from Nucleo.InterfazGraficaProyecto.Logos import cesto_rc
