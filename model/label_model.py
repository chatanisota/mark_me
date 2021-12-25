import cv2
import numpy as np
from classes.label import Label
from copy import copy



class LabelModel:

    __index = 0
    __label = None
    __cursor_point = None       # カーソル（マウス）の場所を示す点

    @staticmethod
    def read_label(label):
        LabelModel.__label = label

    @staticmethod
    def get_label():
        return LabelModel.__label

    @staticmethod
    def regist_mark():
        LabelModel.__label.regist_mark()

    def is_enable_undo():
        return LabelModel.__label.is_enable_undo()

    def undo_mark():
        LabelModel.__label.undo_mark()

    def is_enable_redo():
        return LabelModel.__label.is_enable_redo()

    def redo_mark():
        LabelModel.__label.redo_mark()

    def clear_mark():
        LabelModel.__label.clear_mark()

    # ADD
    @staticmethod
    def add_point(pos):
        LabelModel.set_cursor_point(pos)
        LabelModel.__label.add_mark(LabelModel.__cursor_point)
        LabelModel.__label.add_mark((LabelModel.__cursor_point[0]+0,LabelModel.__cursor_point[1]+1))
        LabelModel.__label.add_mark((LabelModel.__cursor_point[0]+1,LabelModel.__cursor_point[1]+0))
        LabelModel.__label.add_mark((LabelModel.__cursor_point[0]+0,LabelModel.__cursor_point[1]-1))
        LabelModel.__label.add_mark((LabelModel.__cursor_point[0]-1,LabelModel.__cursor_point[1]+0))

    @staticmethod
    def set_cursor_point(pos):
        LabelModel.__cursor_point = pos

    @staticmethod
    def get_cursor_point():
        return LabelModel.__cursor_point

    @staticmethod
    def is_cursoring():
        return not LabelModel.__cursor_point == None

    @staticmethod
    def reset_cursor_point():
        LabelModel.__cursor_point = None

    @staticmethod
    def set_malignancy(level):
        LabelModel.__label.set_malignancy(level)

    @staticmethod
    def get_malignancy():
        return LabelModel.__label.get_malignancy()

    @staticmethod
    def set_comment(text):
        LabelModel.__label.set_comment(text)

    @staticmethod
    def get_comment():
        return LabelModel.__label.get_comment()

    @staticmethod
    def clear_comment():
        LabelModel.__label.set_comment("")

    @staticmethod
    def draw_points(img):
        bleng_img = img.copy()
        color_img = img.copy()
        color_img = cv2.rectangle(color_img, (0, 0), (color_img.shape[0], color_img.shape[1]), (255, 126, 0), thickness=-1)
        trans_img = cv2.addWeighted(color_img, 0.4, bleng_img, 0.6, 0)
        mask = LabelModel.__label.get_mark()
        img = np.where(mask[:, :, np.newaxis] == 0, img, trans_img)
        return img

    @staticmethod
    def draw_cursor(img, pos):
        start = (pos[0], pos[1])
        end = (pos[0] + 8, pos[1] + 8)
        img = cv2.rectangle(img, start, end, (255, 0, 0))
        return img
