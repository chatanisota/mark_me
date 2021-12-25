from model.file_model import FileModel
from model.label_model import LabelModel

class FileController():

    __button_next = None
    __button_prev = None
    __button_complete = None
    __progress_bar = None
    __label_max_index = None


    @staticmethod
    def set_button_next_index(ui):
        FileController.__button_next = ui

    @staticmethod
    def set_button_prev_index(ui):
        FileController.__button_prev = ui

    @staticmethod
    def set_button_complete_index(ui):
        FileController.__button_complete = ui

    @staticmethod
    def set_progress_bar(ui):
        FileController.__progress_bar = ui

    @staticmethod
    def init_open():
        FileModel.load_paths()
        FileController.__progress_bar.setMaximum(FileModel.get_index_num() - 1)

    @staticmethod
    def next_index():
        FileModel.save_json(LabelModel.get_label())
        FileModel.next_index()

    @staticmethod
    def prev_index():
        FileModel.save_json(LabelModel.get_label())
        FileModel.prev_index()

    @staticmethod
    def complete_index():
        exit()

    @staticmethod
    def update_index():
        FileController.__button_prev.setEnabled(not FileModel.is_min_index())
        FileController.__button_next.setEnabled(not FileModel.is_max_index())
        FileController.__button_complete.setEnabled(FileModel.is_max_index())
        FileController.__progress_bar.setValue(FileModel.get_current_index())
