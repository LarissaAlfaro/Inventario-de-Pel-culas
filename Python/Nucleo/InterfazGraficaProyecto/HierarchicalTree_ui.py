# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HierarchicalTree.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(672, 518)
        self.columnView = QtWidgets.QColumnView(Dialog)
        self.columnView.setGeometry(QtCore.QRect(30, 80, 601, 351))
        self.columnView.setObjectName("columnView")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Árbol Jerarquico de Categorías"))
