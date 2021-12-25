from PyQt5.QtGui import QPixmap, QImage, QPalette
from model.image_model import ImageModel
from model.histogram_model import HistogramModel
from model.file_model import FileModel

class ImageController:

    @staticmethod
    def update_from_index():
        update_from_image()

    @staticmethod
    def update_from_file():
        ImageModel.read_slice(FileModel.get_npy())
        img_array = ImageModel.get_pixel_array()
        ImageController.__histogram_filter(img_array)

    @staticmethod
    def update_from_histogram():
        img_array = ImageModel.get_pixel_array()
        ImageController.__histogram_filter(img_array)

    @staticmethod
    def __histogram_filter(img_array):
        #ヒストグラム系
        img_array = HistogramModel.proportional_conversion_8bit(img_array)
        ImageModel.set_array_pixel_hist(img_array)
        ImageController.__color_filter(img_array)

    @staticmethod
    def __color_filter(img_array):
        #カラー化系
        img_array = ImageModel.gray_to_color(img_array)
        ImageModel.set_array_pixel_color(img_array)
