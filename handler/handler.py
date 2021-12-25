from controller.canvas_controller import CanvasController
from controller.histogram_controller import HistogramController
from controller.image_controller import ImageController
from controller.file_controller import FileController
from controller.label_controller import LabelController


class Handler():

    @staticmethod
    def set_label_image(ui):
        CanvasController.set_label_image(ui)

    @staticmethod
    def set_label_original_image(ui):
        CanvasController.set_label_original_image(ui)

    # ヒストグラム
    @staticmethod
    def set_label_histogram(ui):
        HistogramController.set_label_histogram(ui)

    @staticmethod
    def set_slider_max_histogram(ui):
        ui.sliderMoved.connect(Handler.sliderMoved_slider_max_histogram)
        HistogramController.set_slider_max_histogram(ui)

    @staticmethod
    def set_slider_min_histogram(ui):
        ui.sliderMoved.connect(Handler.sliderMoved_slider_min_histogram)
        HistogramController.set_slider_min_histogram(ui)

    @staticmethod
    def set_spin_max_histogram(ui):
        ui.valueChanged.connect(Handler.valueChanged_spin_max_histogram)
        HistogramController.set_spin_max_histogram(ui)

    @staticmethod
    def set_spin_min_histogram(ui):
        ui.valueChanged.connect(Handler.valueChanged_spin_min_histogram)
        HistogramController.set_spin_min_histogram(ui)

    # アノテーション
    @staticmethod
    def set_text_edit_comments(ui):
        ui.textChanged.connect(Handler.textChanged_comment)
        LabelController.set_text_edit_comments(ui)

    @staticmethod
    def set_button_clear_comment(ui):
        ui.clicked.connect(Handler.clicked_button_clear_comment)
        LabelController.set_button_clear_comment(ui)

    @staticmethod
    def set_radio_buttons(uis):
        for ui in uis:
            ui.toggled.connect(Handler.toggled_radio_button)
        LabelController.set_radio_buttons(uis)

    @staticmethod
    def set_button_start_hello(ui):
        ui.clicked.connect(Handler.clicked_button_start_hello)

    # インデックス
    def set_button_next_index(ui):
        ui.clicked.connect(Handler.clicked_button_next_index)
        FileController.set_button_next_index(ui)

    def set_button_prev_index(ui):
        ui.clicked.connect(Handler.clicked_button_prev_index)
        FileController.set_button_prev_index(ui)

    def set_button_complete_index(ui):
        ui.clicked.connect(Handler.clicked_button_complete_index)
        FileController.set_button_complete_index(ui)

    def set_progress_bar(ui):
        FileController.set_progress_bar(ui)

    def set_button_undo_mark(ui):
        ui.clicked.connect(Handler.clicked_button_undo_mark)
        LabelController.set_button_undo_mark(ui)

    def set_button_redo_mark(ui):
        ui.clicked.connect(Handler.clicked_button_redo_mark)
        LabelController.set_button_redo_mark(ui)

    def set_button_clear_mark(ui):
        ui.clicked.connect(Handler.clicked_button_clear_mark)
        LabelController.set_button_clear_mark(ui)

    #----------------------------------------------------------------------
    # 実行部分
    #----------------------------------------------------------------------
    def initialize():
        FileController.init_open()
        Handler.__repaint_from_file()

    # メニューバー
    @staticmethod
    def clicked_button_open():
        FileController.open()
        IndexController.change_image()
        Handler.__repaint()

    @staticmethod
    def clicked_button_save():
        FileController.save()

    @staticmethod
    def clicked_button_save_as_new():
        FileController.save_as_new()


    # ヒストグラム
    @staticmethod
    def sliderMoved_slider_max_histogram():
        HistogramController.change_max_slider()
        Handler.__repaint_from_histogram()

    @staticmethod
    def sliderMoved_slider_min_histogram():
        HistogramController.change_min_slider()
        Handler.__repaint_from_histogram()

    @staticmethod
    def valueChanged_spin_max_histogram():
        HistogramController.change_max_spin()
        Handler.__repaint_from_histogram()

    @staticmethod
    def valueChanged_spin_min_histogram():
        HistogramController.change_min_spin()
        Handler.__repaint_from_histogram()


    # 描写画面内
    @staticmethod
    def canvas_mouse_press(x, y):
        LabelController.pen_down(x, y)
        Handler.__repaint_from_marker()

    @staticmethod
    def canvas_mouse_release(x, y):
        LabelController.pen_drag(x, y)
        Handler.__repaint_from_marker()

    @staticmethod
    def canvas_mouse_move(x, y):
        LabelController.pen_air(x, y)
        Handler.__repaint_from_cursor()

    @staticmethod
    def canvas_mouse_drag(x, y):
        LabelController.pen_drag(x, y)
        Handler.__repaint_from_marker()

    # マーク
    def clicked_button_undo_mark():
        LabelController.undo_mark()
        Handler.__repaint_from_marker()

    def clicked_button_redo_mark():
        LabelController.redo_mark()
        Handler.__repaint_from_marker()

    def clicked_button_clear_mark():
        LabelController.clear_mark()
        Handler.__repaint_from_marker()

    # アノテーション
    def clicked_button_clear_comment():
        LabelController.clear_comment()
        LabelController.update_comment()

    def toggled_radio_button():
        LabelController.toggle_malignancy()
        LabelController.update_malignancy()

    def textChanged_comment():
        LabelController.change_comment()
        # LabelController.update_comment()

    # インデックス
    def clicked_button_next_index():
        FileController.next_index()
        Handler.__repaint_from_file()

    def clicked_button_prev_index():
        FileController.prev_index()
        Handler.__repaint_from_file()

    def clicked_button_complete_index():
        exit()

    #private
    @staticmethod
    def __repaint_from_file():
        FileController.update_index()
        ImageController.update_from_file()
        LabelController.update_from_file()
        HistogramController.update_from_file()
        CanvasController.update_from_maker()

    @staticmethod
    def __repaint_from_histogram():
        ImageController.update_from_histogram()
        LabelController.update_from_maker()
        HistogramController.update_from_histogram()
        CanvasController.update_from_maker()

    def __repaint_from_marker():
        CanvasController.update_from_maker()
        LabelController.update_from_maker()

    def __repaint_from_cursor():
        CanvasController.update_from_cursor()
