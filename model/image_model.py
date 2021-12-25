
from PyQt5.QtGui import QPixmap, QImage
import numpy as np
import cv2

class ImageModel():

    __pixel_array       = np.zeros((100,100))
    __pixel_array_hist  = None
    __pixel_array_color = None
    __pixel_array_canvas_maker = None
    __pixel_array_canvas_zoom = None
    __pixel_array_canvas_cursor = None
    __pixel_array_original_zoom = None
    __pixel_array_original_cursor = None

    @staticmethod
    def read_slice(slice):
        ImageModel.__pixel_array      = slice

    @staticmethod
    def calc_whole_histogram(histogram_window_width):
        hists ,_ = np.histogram(ImageModel.__pixel_array, bins=histogram_window_width, range=(0,1400))
        hists = hists.astype(np.float) / hists.max()
        return hists

    @staticmethod
    def gray_to_color(img_array):
        return cv2.cvtColor(img_array, cv2.COLOR_GRAY2RGB)

    @staticmethod
    def get_size():
        return ImageModel.__pixel_array.shape

    @staticmethod
    def get_pixel_array():
        return ImageModel.__pixel_array

    @staticmethod
    def set_array_pixel_hist(img):
        ImageModel.__pixel_array_hist = img.copy()

    @staticmethod
    def set_array_pixel_color(img):
        ImageModel.__pixel_array_color = img.copy()

    @staticmethod
    def set_array_pixel_canvas_maker(img):
        ImageModel.__pixel_array_canvas_maker = img.copy()

    @staticmethod
    def set_array_pixel_canvas_zoom(img):
        ImageModel.__pixel_array_canvas_zoom = img.copy()

    @staticmethod
    def set_array_pixel_original_zoom(img):
        ImageModel.__pixel_array_original_zoom = img.copy()

    @staticmethod
    def set_array_pixel_canvas_cursor(img):
        ImageModel.__pixel_array_canvas_cursor = img.copy()

    @staticmethod
    def set_array_pixel_original_cursor(img):
        ImageModel.__pixel_array_original_cursor = img.copy()

    # setter
    @staticmethod
    def set_array_pixel_map_maker(img):
        ImageModel.__pixel_array_map_maker = img.copy()

    @staticmethod
    def get_array_pixel_hist():
        return ImageModel.__pixel_array_hist.copy()

    @staticmethod
    def get_array_pixel_color():
        return ImageModel.__pixel_array_color.copy()

    @staticmethod
    def get_array_pixel_canvas_maker():
        return ImageModel.__pixel_array_canvas_maker.copy()

    @staticmethod
    def get_array_pixel_canvas_zoom():
        return ImageModel.__pixel_array_canvas_zoom.copy()

    @staticmethod
    def get_array_pixel_original_zoom():
        return ImageModel.__pixel_array_original_zoom.copy()

    @staticmethod
    def get_array_pixel_canvas_cursor():
        return ImageModel.__pixel_array_canvas_cursor.copy()

    @staticmethod
    def get_array_pixel_original_cursor():
        return ImageModel.__pixel_array_original_cursor.copy()
