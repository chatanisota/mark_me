from model.map_model import MapModel
from model.label_model import LabelModel
from model.file_model import FileModel
from model.image_model import ImageModel
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QAbstractItemView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from classes.label import Label



class LabelController:


    __text_edit_comments = None
    __radio_buttons = None
    __button_undo = None
    __button_redo = None
    __button_clear = None


    @staticmethod
    def set_text_edit_comments(ui):
        LabelController.__text_edit_comments = ui

    @staticmethod
    def set_button_clear_comment(ui):
        LabelController.__button_clear = ui

    @staticmethod
    def set_radio_buttons(uis):
        LabelController.__radio_buttons = uis

    @staticmethod
    def set_button_undo_mark(ui):
        LabelController.__button_undo = ui

    @staticmethod
    def set_button_redo_mark(ui):
        LabelController.__button_redo = ui

    @staticmethod
    def set_button_clear_mark(ui):
        LabelController.__button_clear = ui

    @staticmethod
    def pen_down(x, y):
        LabelModel.regist_mark()
        LabelController.pen_drag(x, y)

    @staticmethod
    def pen_drag(x, y):
        temp_pos = MapModel.click_pos_to_image_pos((x, y))
        if(not LabelController.is_in_range(temp_pos)):
            LabelModel.reset_cursor_point()
            return
        LabelModel.add_point(temp_pos)

    @staticmethod
    def pen_air(x, y):
        temp_pos = MapModel.click_pos_to_image_pos((x, y))
        if(not LabelController.is_in_range(temp_pos)):
            LabelModel.reset_cursor_point()
            return
        LabelModel.set_cursor_point(temp_pos)

    @staticmethod
    def toggle_malignancy():
        malignant_level = LabelController.__get_malignant_level()
        LabelModel.set_malignancy(malignant_level)

    @staticmethod
    def change_comment():
        text = LabelController.__text_edit_comments.toPlainText()
        LabelModel.set_comment(text)

    @staticmethod
    def clear_comment():
        LabelModel.clear_comment()


    @staticmethod
    def is_in_range(pos):
        size = ImageModel.get_size()
        return pos[0]>=0 and pos[0]<size[0] and pos[1]>=0 and pos[1]<size[1]

    @staticmethod
    def undo_mark():
        LabelModel.undo_mark()

    @staticmethod
    def redo_mark():
        LabelModel.redo_mark()

    @staticmethod
    def clear_mark():
        LabelModel.clear_mark()


    @staticmethod
    def __get_malignant_level():
        malignant_level = 0
        for i, radio in enumerate(LabelController.__radio_buttons):
            if radio.isChecked() == True:
                malignant_level = i + 1
        return malignant_level

    @staticmethod
    def __get_comments():
        return LabelController.__text_edit_comments.toPlainText()

    @staticmethod
    def update_from_file():
        LabelModel.read_label(FileModel.get_label(ImageModel.get_size()))
        LabelController.update_malignancy()
        LabelController.update_comment()
        LabelController.update_from_maker()

    @staticmethod
    def update_from_maker():
        LabelController.__button_undo.setEnabled(LabelModel.is_enable_undo())
        LabelController.__button_redo.setEnabled(LabelModel.is_enable_redo())

    @staticmethod
    def update_malignancy():
        for i in range(len(LabelController.__radio_buttons)):
            LabelController.__radio_buttons[i].setChecked((i+1) == LabelModel.get_malignancy())

    @staticmethod
    def update_comment():
        text = LabelModel.get_comment()
        LabelController.__text_edit_comments.blockSignals(True)
        LabelController.__text_edit_comments.setPlainText(text)
        LabelController.__text_edit_comments.blockSignals(False)
