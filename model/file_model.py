import glob
import tqdm
import os

import json
import collections as cl
import numpy as np
from classes.label import Label
import cv2

class FileModel:


    __npy_folder = './datas/'
    __json_folder = './please_send_this_folder/'
    __names = []
    __current_index = 0




    @staticmethod
    def get_index_num():
        return len(FileModel.__names)

    @staticmethod
    def set_current_index(index):
        FileModel.__current_index = index

    @staticmethod
    def get_current_index():
        return FileModel.__current_index

    @staticmethod
    def is_min_index():
        return FileModel.__current_index <= 0

    @staticmethod
    def is_max_index():
        return FileModel.__current_index >= (FileModel.get_index_num() - 1)

    @staticmethod
    def next_index():
        if not FileModel.is_max_index():
            FileModel.__current_index += 1

    @staticmethod
    def prev_index():
        if not FileModel.is_min_index():
            FileModel.__current_index -= 1

    @staticmethod
    def load_paths():
        paths = glob.glob(FileModel.__npy_folder + '*')
        paths = [os.path.splitext(os.path.basename(path))[0] for path in paths]
        FileModel.__names = paths

    @staticmethod
    def get_npy():
        img = FileModel.open_npy(FileModel.__npy_folder + FileModel.__names[FileModel.__current_index]+'.npy')
        return img

    @staticmethod
    def get_label(size):
        print(FileModel.__json_folder + FileModel.__names[FileModel.__current_index]+'.json')
        label = FileModel.open_json(FileModel.__json_folder + FileModel.__names[FileModel.__current_index]+'.json', size)
        return label

    @staticmethod
    def open_npy(npy_path):
        img = np.load(npy_path)
        return (img * 1400).astype(np.int16)

    @staticmethod
    def open_json(json_path, size):
        if(not os.path.isfile(json_path)):
            print("no file")
            label = Label(size)
            print(label.get_mark())
            return label

        with open(json_path) as f:
            df = json.load(f)

        label_json = df["label"]
        label = Label(size)
        label.set_json(label_json)
        return label


    @staticmethod
    def save_json(label):
        ys = cl.OrderedDict()
        nodule_me_json = cl.OrderedDict()
        ys["label"] = label.get_json()
        fw = open(FileModel.__json_folder + FileModel.__names[FileModel.__current_index]+'.json','w')
        json.dump(ys, fw, indent=4)
