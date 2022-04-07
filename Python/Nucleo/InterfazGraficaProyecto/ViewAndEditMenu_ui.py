# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ViewAndEditMenu.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(694, 464)
        Dialog.setStyleSheet("background-color:rgb(165, 233, 255);")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 651, 361))
        self.textEdit.setAcceptDrops(True)
        self.textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit.setStyleSheet("background-color:rgb(255,255,255);")
        self.textEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.textEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 390, 161, 51))
        self.pushButton_2.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(252, 204, 50);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(80, 390, 291, 61))
        self.lineEdit.setStyleSheet("background-color:rgb(255,255,255);\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 390, 91, 51))
        self.pushButton_3.setStyleSheet("border-style: solid;\n"
"image: url(:/cesto/1f5d1.png);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(225, 89, 123);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ver y Editar Peliculas"))
        self.pushButton_2.setText(_translate("Dialog", "Editar"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Id de la Película que desea Borrar o Editar."))
        self.pushButton_3.setToolTip(_translate("Dialog", "<html><head/><body><p><img src=\":/cesto/1f5d1.png\"/></p></body></html>"))
from Nucleo.InterfazGraficaProyecto.Logos import cesto_rc
