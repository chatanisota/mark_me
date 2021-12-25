import cv2
import numpy as np

class MapModel:

    __start_pos_x = 0
    __start_pos_y = 0
    __drag_start_point = (0,0)

    __zoom_scale = 1.0
    __MAX_ZOOM_SCALE = 64.0
    __MIN_ZOOM_SCALE = 0.5
    __ZOOM_SCALE = (8,8)

    @staticmethod
    def zoom(img_array):
        img_array = cv2.resize(img_array, dsize=MapModel.get_dsize(img_array), interpolation=cv2.INTER_NEAREST)   #バイリニア補間（ふつう）
        return img_array

    @staticmethod
    def get_dsize(img_array):
        return (img_array.shape[0] * MapModel.__ZOOM_SCALE[0], img_array.shape[1] * MapModel.__ZOOM_SCALE[1])


    @staticmethod
    def click_pos_to_image_pos(point_pos):
        #クリックされた場所 / マップの大きさ (この時点で、0-1:画像全体の何パーセント時点か) * キャンバスの大きさ
        target_pos_x = int(round(point_pos[0] / MapModel.__ZOOM_SCALE[0])) - 2
        target_pos_y = int(round(point_pos[1] / MapModel.__ZOOM_SCALE[1])) - 3
        return (target_pos_x, target_pos_y)

    @staticmethod
    def image_pos_to_canvas_pos(point_pos):
        target_pos_x = int(round(point_pos[0] * MapModel.__ZOOM_SCALE[0]))
        target_pos_y = int(round(point_pos[1] * MapModel.__ZOOM_SCALE[1]))
        return (target_pos_x, target_pos_y)
