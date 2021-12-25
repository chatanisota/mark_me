import numpy as np
from PyQt5.QtGui import QPixmap, QImage, QPalette
from model.histogram_model import HistogramModel
from model.image_model import ImageModel

class HistogramController:

    __label_histogram = None
    __slider_max_histogram = None
    __slider_min_histogram = None
    __spin_max_histogram = None
    __spin_min_histogram = None

    @staticmethod
    def set_label_histogram(label_histogram):
        HistogramController.__label_histogram = label_histogram
        HistogramController.__repaint()

    @staticmethod
    def set_slider_max_histogram(slider_max_histogram):
        HistogramController.__slider_max_histogram = slider_max_histogram
        HistogramController.__slider_max_histogram.setMinimum(-1000)
        HistogramController.__slider_max_histogram.setMaximum(400)
        HistogramController.__slider_max_histogram.setValue(HistogramModel.get_max())


    @staticmethod
    def set_slider_min_histogram(slider_min_histogram):
        HistogramController.__slider_min_histogram = slider_min_histogram
        HistogramController.__slider_min_histogram.setMinimum(-1000)
        HistogramController.__slider_min_histogram.setMaximum(400)
        HistogramController.__slider_min_histogram.setValue(HistogramModel.get_min())

    @staticmethod
    def set_spin_max_histogram(ui):
        HistogramController.__spin_max_histogram = ui
        HistogramController.__spin_max_histogram.setMinimum(-1000)
        HistogramController.__spin_max_histogram.setMaximum(400)
        HistogramController.__spin_max_histogram.blockSignals(True)
        HistogramController.__spin_max_histogram.setValue(HistogramModel.get_max())
        HistogramController.__spin_max_histogram.blockSignals(False)

    @staticmethod
    def set_spin_min_histogram(ui):
        HistogramController.__spin_min_histogram = ui
        HistogramController.__spin_min_histogram.setMinimum(-1000)
        HistogramController.__spin_min_histogram.setMaximum(400)
        HistogramController.__spin_min_histogram.blockSignals(True)
        HistogramController.__spin_min_histogram.setValue(HistogramModel.get_min())
        HistogramController.__spin_min_histogram.blockSignals(False)

    @staticmethod
    def change_max_slider():
        max = HistogramController.__slider_max_histogram.value()
        HistogramModel.set_max(max)
        HistogramController.__slider_min_histogram.setValue(HistogramModel.get_min())
        HistogramController.__spin_min_histogram.blockSignals(True)
        HistogramController.__spin_max_histogram.blockSignals(True)
        HistogramController.__spin_min_histogram.setValue(HistogramModel.get_min())
        HistogramController.__spin_max_histogram.setValue(HistogramModel.get_max())
        HistogramController.__spin_min_histogram.blockSignals(False)
        HistogramController.__spin_max_histogram.blockSignals(False)

    @staticmethod
    def change_min_slider():
        min = HistogramController.__slider_min_histogram.value()
        HistogramModel.set_min(min)
        HistogramController.__slider_max_histogram.setValue(HistogramModel.get_max())
        HistogramController.__spin_min_histogram.blockSignals(True)
        HistogramController.__spin_max_histogram.blockSignals(True)
        HistogramController.__spin_min_histogram.setValue(HistogramModel.get_min())
        HistogramController.__spin_max_histogram.setValue(HistogramModel.get_max())
        HistogramController.__spin_min_histogram.blockSignals(False)
        HistogramController.__spin_max_histogram.blockSignals(False)

    @staticmethod
    def change_max_spin():
        max = HistogramController.__spin_max_histogram.value()
        HistogramModel.set_max(max)
        HistogramController.__slider_max_histogram.setValue(HistogramModel.get_max())
        HistogramController.__slider_min_histogram.setValue(HistogramModel.get_min())
        HistogramController.__spin_min_histogram.blockSignals(True)
        HistogramController.__spin_min_histogram.setValue(HistogramModel.get_min())
        HistogramController.__spin_min_histogram.blockSignals(False)

    @staticmethod
    def change_min_spin():
        min = HistogramController.__spin_min_histogram.value()
        HistogramModel.set_min(min)
        HistogramController.__slider_max_histogram.setValue(HistogramModel.get_max())
        HistogramController.__slider_min_histogram.setValue(HistogramModel.get_min())
        HistogramController.__spin_max_histogram.blockSignals(True)
        HistogramController.__spin_max_histogram.setValue(HistogramModel.get_max())
        HistogramController.__spin_max_histogram.blockSignals(False)

    @staticmethod
    def update_from_file():
        HistogramController.__repaint()

    @staticmethod
    def update_from_histogram():
        HistogramController.__repaint()

    @staticmethod
    def __repaint():
        #画像生成
        hists   = ImageModel.calc_whole_histogram(HistogramModel.get_window_width())
        qimg    = HistogramModel.create_qimg(hists)
        HistogramController.__label_histogram.setPixmap(QPixmap.fromImage(qimg))
