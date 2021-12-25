# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_label.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LabelDialog(object):
    def setupUi(self, LabelDialog):
        LabelDialog.setObjectName("LabelDialog")
        LabelDialog.resize(349, 257)
        self.radioButton5 = QtWidgets.QRadioButton(LabelDialog)
        self.radioButton5.setGeometry(QtCore.QRect(20, 40, 86, 16))
        self.radioButton5.setObjectName("radioButton5")
        self.radioButton4 = QtWidgets.QRadioButton(LabelDialog)
        self.radioButton4.setGeometry(QtCore.QRect(20, 60, 86, 16))
        self.radioButton4.setObjectName("radioButton4")
        self.radioButton3 = QtWidgets.QRadioButton(LabelDialog)
        self.radioButton3.setGeometry(QtCore.QRect(20, 80, 86, 16))
        self.radioButton3.setObjectName("radioButton3")
        self.radioButton2 = QtWidgets.QRadioButton(LabelDialog)
        self.radioButton2.setGeometry(QtCore.QRect(20, 100, 86, 16))
        self.radioButton2.setObjectName("radioButton2")
        self.radioButton1 = QtWidgets.QRadioButton(LabelDialog)
        self.radioButton1.setGeometry(QtCore.QRect(20, 120, 86, 16))
        self.radioButton1.setObjectName("radioButton1")
        self.label_2 = QtWidgets.QLabel(LabelDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 111, 16))
        self.label_2.setObjectName("label_2")
        self.buttonCancel = QtWidgets.QPushButton(LabelDialog)
        self.buttonCancel.setGeometry(QtCore.QRect(250, 220, 75, 23))
        self.buttonCancel.setObjectName("buttonCancel")
        self.buttonOk = QtWidgets.QPushButton(LabelDialog)
        self.buttonOk.setGeometry(QtCore.QRect(160, 220, 75, 23))
        self.buttonOk.setText("OK")
        self.buttonOk.setObjectName("buttonOk")
        self.textEditComments = QtWidgets.QPlainTextEdit(LabelDialog)
        self.textEditComments.setGeometry(QtCore.QRect(130, 40, 201, 91))
        self.textEditComments.setObjectName("textEditComments")
        self.label_3 = QtWidgets.QLabel(LabelDialog)
        self.label_3.setGeometry(QtCore.QRect(130, 10, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(LabelDialog)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 81, 21))
        self.label_4.setObjectName("label_4")
        self.comboBoxNoduleId = QtWidgets.QComboBox(LabelDialog)
        self.comboBoxNoduleId.setGeometry(QtCore.QRect(20, 180, 311, 22))
        self.comboBoxNoduleId.setObjectName("comboBoxNoduleId")

        self.retranslateUi(LabelDialog)
        QtCore.QMetaObject.connectSlotsByName(LabelDialog)

    def retranslateUi(self, LabelDialog):
        _translate = QtCore.QCoreApplication.translate
        LabelDialog.setWindowTitle(_translate("LabelDialog", "Dialog"))
        self.radioButton5.setText(_translate("LabelDialog", "5"))
        self.radioButton4.setText(_translate("LabelDialog", "4"))
        self.radioButton3.setText(_translate("LabelDialog", "3"))
        self.radioButton2.setText(_translate("LabelDialog", "2"))
        self.radioButton1.setText(_translate("LabelDialog", "1"))
        self.label_2.setText(_translate("LabelDialog", "Malignant level"))
        self.buttonCancel.setText(_translate("LabelDialog", "Cancel"))
        self.label_3.setText(_translate("LabelDialog", "Comments"))
        self.label_4.setText(_translate("LabelDialog", "Nodule id"))

