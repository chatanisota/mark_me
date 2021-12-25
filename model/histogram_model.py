
from PyQt5.QtGui import QPixmap, QImage
import cv2
import numpy as np

class HistogramModel():

    #表示部分
    __qimg              = None
    __img_array         = None
    __img_width         = 300
    __img_height        = 150
    __img_bytesPerLine  = 1                             #const
    __img_mode          = QImage.Format_Grayscale8      #const
    #データ部分
    __img_min           = -1000
    __img_max           = 400

    @staticmethod
    def create_qimg(hists):
        img_array = np.full((HistogramModel.__img_height, HistogramModel.__img_width),255,np.uint8)
        img_array = HistogramModel.__draw_whole_hists(img_array, hists)
        img_array = HistogramModel.__draw_line(img_array)

        return QImage(img_array, HistogramModel.__img_width, HistogramModel.__img_height, HistogramModel.__img_width * HistogramModel.__img_bytesPerLine, HistogramModel.__img_mode)

    @staticmethod
    def __draw_line(img):
        min = int( HistogramModel.__img_width * (HistogramModel.__img_min + 1000) / 1400 )
        max = int( HistogramModel.__img_width * (HistogramModel.__img_max + 1000) / 1400 )
        img = cv2.line(img,(0,HistogramModel.__img_height-1),(min,HistogramModel.__img_height-1),0,1)
        img = cv2.line(img,(min,HistogramModel.__img_height-1),(max,0),0,1)
        img = cv2.line(img,(max,0),(HistogramModel.__img_width,0),0,1)
        return img

    @staticmethod
    def __draw_whole_hists(img, hists):
        for i, hist in enumerate(hists):
            img = cv2.line(img,(i,HistogramModel.__img_height-1),(i,HistogramModel.__img_height-1 - int( hist * (HistogramModel.__img_height-1))),100,2)
        return img

    #比例変換により8bitに正規化
    @staticmethod
    def proportional_conversion_8bit(img_array):
        min = int( HistogramModel.__img_min + 1000)
        max = int( HistogramModel.__img_max + 1000)
        img_array = np.clip(img_array, min, max)
        #上限下限範囲外を全て0に
        #範囲を 0 ~ (-min+max)に
        img_array = img_array - min
        img_array = img_array.astype(np.float64) / (HistogramModel.__img_max - HistogramModel.__img_min) * 255  #8bitに正規化
        img_array = img_array.astype(np.uint8)
        #print(img_array)
        #exit()
        return img_array

    @staticmethod
    def get_max():
        return HistogramModel.__img_max

    @staticmethod
    def get_min():
        return HistogramModel.__img_min

    @staticmethod
    def get_window_width():
        return HistogramModel.__img_width

    @staticmethod
    def set_max(max):
        if(max>-1000):
            HistogramModel.__img_max = max
            if(max <= HistogramModel.__img_min):
                 HistogramModel.__img_min = max - 1

    @staticmethod
    def set_min(min):
        if(min<400):
            HistogramModel.__img_min = min
            if(min > HistogramModel.__img_max):
                 HistogramModel.__img_max = min + 1
