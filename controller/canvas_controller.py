from PyQt5.QtGui import QPixmap, QImage, QPalette
from model.image_model import ImageModel
from model.histogram_model import HistogramModel
from model.map_model import MapModel
from model.label_model import LabelModel
import numpy as np


class CanvasController:

    __label_image = None
    __label_original_image = None

    @staticmethod
    def set_label_image(ui):
        CanvasController.__label_image = ui
        # スケールは1.0
        CanvasController.__label_image.scaleFactor = 1.0

        image = QImage()
        # ラベルに読み込んだ画像を反映
        CanvasController.__label_image.setPixmap(QPixmap.fromImage(image))

    @staticmethod
    def set_label_original_image(ui):
        CanvasController.__label_original_image = ui
        # スケールは1.0
        CanvasController.__label_original_image.scaleFactor = 1.0

        image = QImage()
        # ラベルに読み込んだ画像を反映
        CanvasController.__label_original_image.setPixmap(QPixmap.fromImage(image))

    @staticmethod
    def update_from_maker():
        img_array = ImageModel.get_array_pixel_color()
        CanvasController.__maker_filter(img_array)
        CanvasController.__original_zoom_filter(img_array)

    @staticmethod
    def update_from_cursor():
        img_array = ImageModel.get_array_pixel_canvas_zoom()
        CanvasController.__cursor_filter(img_array)
        img_array2 = ImageModel.get_array_pixel_original_zoom()
        CanvasController.__original_cursor_filter(img_array2)

    @staticmethod
    def __maker_filter(img_array):
        # マーカ系
        img_array = LabelModel.draw_points(img_array)
        ImageModel.set_array_pixel_canvas_maker(img_array)
        CanvasController.__zoom_filter(img_array)

    @staticmethod
    def __zoom_filter(img_array):
        #ズーム系
        img_array = MapModel.zoom(img_array)
        ImageModel.set_array_pixel_canvas_zoom(img_array)
        CanvasController.__cursor_filter(img_array)

    @staticmethod
    def __cursor_filter(img_array):
        # カーソル系
        if(LabelModel.is_cursoring()):
            img_array = LabelModel.draw_cursor(img_array, MapModel.image_pos_to_canvas_pos(LabelModel.get_cursor_point()))
        ImageModel.set_array_pixel_canvas_cursor(img_array)
        CanvasController.__repaint(img_array)

    @staticmethod
    def __original_zoom_filter(img_array):
        #ズーム系
        img_array = MapModel.zoom(img_array)
        ImageModel.set_array_pixel_original_zoom(img_array)
        CanvasController.__original_cursor_filter(img_array)

    @staticmethod
    def __original_cursor_filter(img_array):
        # カーソル系
        if(LabelModel.is_cursoring()):
            img_array = LabelModel.draw_cursor(img_array, MapModel.image_pos_to_canvas_pos(LabelModel.get_cursor_point()))
        ImageModel.set_array_pixel_original_cursor(img_array)
        CanvasController.__original_repaint(img_array)



    @staticmethod
    def __repaint(img):
        #画像生成
        qimg = QImage(img, img.shape[1], img.shape[0], img.shape[1] * 3, QImage.Format_RGB888)
        CanvasController.__label_image.setPixmap(QPixmap.fromImage(qimg))

    @staticmethod
    def __original_repaint(img):
        #画像生成
        qimg = QImage(img, img.shape[1], img.shape[0], img.shape[1] * 3, QImage.Format_RGB888)
        CanvasController.__label_original_image.setPixmap(QPixmap.fromImage(qimg))
