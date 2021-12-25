# pyuic5 ui_message.ui -o ui_message.py

from PyQt5.QtWidgets import QDialog
from qt_designer.ui_message import *

class MessageDialog(QDialog):

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_MessageDialog()
        self.ui.setupUi(self)

        self.ui.buttonMessageDialog.clicked.connect(lambda: self.close(self))

    @staticmethod
    def open(self, text):
        self.ui.labelMessageDialog.setText(text)
        if(not self.isVisible()):
            self.show()

    @staticmethod
    def close(self):
        print("aa",self)
        if(self.isVisible()):
            self.accept()
