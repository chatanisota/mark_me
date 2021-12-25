# pyinstaller mark_me.py --onefile --noconsole --icon=mark_me.ico
# pyuic5 ./qt_designer/ui_markme.ui -o ./qt_designer/ui_markme.py
# pyuic5 ui_label.ui -o ui_label.py
# pyuic5 ui_pen.ui -o ui_pen.py
# pyuic5 ui_hello.ui -o ui_hello.py

import sys, os
import glob
from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QButtonGroup
from PyQt5.QtGui import QPixmap, QImage, QPalette
from PyQt5.QtCore import Qt
import cv2
import numpy as np
from qt_designer.ui_markme import *
from handler.handler import Handler




class MyForm(QWidget):

    __is_finish_init = False

    def __init__(self, parent=None):
        super().__init__()

        # ダイアログの設定
        self.setWindowFlags(
            Qt.Window|
            Qt.WindowMinimizeButtonHint|
            Qt.WindowCloseButtonHint
            )

        # 起動時の画像
        img = cv2.imread("./ui/wait_image.png")
        cv2.imshow("wait please...", img)
        cv2.waitKey(1)

        super(MyForm, self).__init__(parent)
        print("== SETTING Main Dialog ==")

        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)

        print("== Handler setting... ==")
        #ハンドラのセット
        # Handler.set_main_dialog(self)
        Handler.set_label_image(self.ui.labelImage)
        Handler.set_label_original_image(self.ui.labelOriginal)
        Handler.set_label_histogram(self.ui.labelHistogram)
        Handler.set_slider_max_histogram(self.ui.sliderMaxHistogram)
        Handler.set_slider_min_histogram(self.ui.sliderMinHistogram)
        Handler.set_spin_min_histogram(self.ui.spinMinHistogram)
        Handler.set_spin_max_histogram(self.ui.spinMaxHistogram)
        Handler.set_button_next_index(self.ui.buttonNextIndex)
        Handler.set_button_prev_index(self.ui.buttonPrevIndex)
        Handler.set_button_complete_index(self.ui.buttonCompleteIndex)
        Handler.set_button_undo_mark(self.ui.buttonUndoMark)
        Handler.set_button_redo_mark(self.ui.buttonRedoMark)
        Handler.set_button_clear_mark(self.ui.buttonClearMark)
        Handler.set_progress_bar(self.ui.progressBarIndex)

        self.group = QButtonGroup()
        self.group.addButton(self.ui.radioButton1,1)
        self.group.addButton(self.ui.radioButton2,2)
        self.group.addButton(self.ui.radioButton3,3)
        self.group.addButton(self.ui.radioButton4,4)
        self.group.addButton(self.ui.radioButton5,5)
        Handler.set_radio_buttons([
            self.ui.radioButton1,
            self.ui.radioButton2,
            self.ui.radioButton3,
            self.ui.radioButton4,
            self.ui.radioButton5,
            ])
        Handler.set_text_edit_comments(self.ui.textEditComment)
        Handler.set_button_clear_comment(self.ui.buttonClearComment)

        print("== Handler set complete! ==")

        cv2.destroyAllWindows()

        Handler.initialize()
        MyForm.__is_finish_init = True


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
