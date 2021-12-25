# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_hello.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HelloDialog(object):
    def setupUi(self, HelloDialog):
        HelloDialog.setObjectName("HelloDialog")
        HelloDialog.setWindowModality(QtCore.Qt.WindowModal)
        HelloDialog.resize(309, 97)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../nodule_me.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HelloDialog.setWindowIcon(icon)
        self.buttonStartHello = QtWidgets.QPushButton(HelloDialog)
        self.buttonStartHello.setGeometry(QtCore.QRect(190, 50, 101, 31))
        self.buttonStartHello.setStyleSheet("")
        self.buttonStartHello.setObjectName("buttonStartHello")
        self.comboBoxUserHello = QtWidgets.QComboBox(HelloDialog)
        self.comboBoxUserHello.setGeometry(QtCore.QRect(10, 50, 161, 31))
        self.comboBoxUserHello.setObjectName("comboBoxUserHello")
        self.label = QtWidgets.QLabel(HelloDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 221, 21))
        self.label.setObjectName("label")

        self.retranslateUi(HelloDialog)
        QtCore.QMetaObject.connectSlotsByName(HelloDialog)

    def retranslateUi(self, HelloDialog):
        _translate = QtCore.QCoreApplication.translate
        HelloDialog.setWindowTitle(_translate("HelloDialog", "Hello nodule_me!"))
        self.buttonStartHello.setText(_translate("HelloDialog", "Start"))
        self.label.setText(_translate("HelloDialog", "Please select current USER."))

