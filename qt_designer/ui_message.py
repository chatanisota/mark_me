# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_message.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MessageDialog(object):
    def setupUi(self, MessageDialog):
        MessageDialog.setObjectName("MessageDialog")
        MessageDialog.setWindowModality(QtCore.Qt.WindowModal)
        MessageDialog.resize(273, 73)
        self.verticalLayout = QtWidgets.QVBoxLayout(MessageDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelMessageDialog = QtWidgets.QLabel(MessageDialog)
        self.labelMessageDialog.setObjectName("labelMessageDialog")
        self.verticalLayout.addWidget(self.labelMessageDialog)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonMessageDialog = QtWidgets.QPushButton(MessageDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonMessageDialog.sizePolicy().hasHeightForWidth())
        self.buttonMessageDialog.setSizePolicy(sizePolicy)
        self.buttonMessageDialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.buttonMessageDialog.setObjectName("buttonMessageDialog")
        self.horizontalLayout.addWidget(self.buttonMessageDialog)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(MessageDialog)
        QtCore.QMetaObject.connectSlotsByName(MessageDialog)

    def retranslateUi(self, MessageDialog):
        _translate = QtCore.QCoreApplication.translate
        MessageDialog.setWindowTitle(_translate("MessageDialog", "Nodule me - Message"))
        self.labelMessageDialog.setText(_translate("MessageDialog", "TextLabel"))
        self.buttonMessageDialog.setText(_translate("MessageDialog", "Ok"))

