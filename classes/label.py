import numpy as np
import collections as cl

import copy

class Label:

    def __init__(self, size):
        self.__size = size
        self.__marks = []
        self.__comment = ""
        self.__malignancy = 3
        self.__index = 0
        self.__marks.append(np.zeros((size[1], size[0]), np.int8))
        print(self.get_mark())

    def regist_mark(self):

        temp = []
        temp.append(self.__marks[self.__index])
        for mark in self.__marks[self.__index:]:
            temp.append(mark.copy())
        self.__marks = temp
        self.__index = 0

    def add_mark(self, point):
        if point[1] >= 0 and point[0] >= 0 and point[1] < self.__size[1] and point[0] < self.__size[0]:
            self.__marks[0][point[1], point[0]] = 1

    def undo_mark(self):
        if self.is_enable_undo():
            self.__index += 1

    def is_enable_undo(self):
        return self.__index + 1 < len(self.__marks)

    def redo_mark(self):
        if self.is_enable_redo():
            self.__index -= 1

    def is_enable_redo(self):
        return self.__index > 0

    def clear_mark(self):
        self.__index = 0
        self.__marks = []
        self.__marks.append(np.zeros((self.__size[0], self.__size[1]), np.int8))

    def get_mark(self):
        return self.__marks[self.__index]

    def set_malignancy(self, level):
        self.__malignancy = level

    def get_malignancy(self):
        return self.__malignancy

    def set_comment(self, text):
        self.__comment = text

    def get_comment(self):
        return self.__comment


    #書き込み用
    def get_json(self):
        json = cl.OrderedDict()
        json["malignancy"] = self.__malignancy
        json["comment"] = self.__comment
        json["marks"] = self.get_mark().tolist()
        return json

    #読み込み用
    def set_json(self, json):
        self.__index = 0
        self.__marks = []
        self.__marks.append(np.array(json["marks"]))
        self.__malignancy = int(json["malignancy"])
        self.__comment = json["comment"]
