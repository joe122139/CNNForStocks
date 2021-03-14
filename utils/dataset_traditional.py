from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import os
from collections import defaultdict
import numpy as np
import scipy.misc
from matplotlib.pyplot import imread
import cv2


def dataset(base_dir, n):
    print("trad. base_dir : {}, n : {}".format(base_dir, n))
    d = defaultdict(list)
    for root, subdirs, files in os.walk(base_dir):
        for filename in files:
            file_path = os.path.join(root, filename)
            assert file_path.startswith(base_dir)
            suffix = file_path[len(base_dir):]
            suffix = suffix.lstrip("\\")
            label = suffix.split("\\")[0]
            d[label].append(file_path)

    tags = sorted(d.keys())
    # print("classes : {}".format(tags))
    # useful_image_count = 0

    X = []
    y = []

    for class_index, class_name in enumerate(tags):
        filenames = d[class_name]
        for filename in filenames:
            #img = scipy.misc.imread(filename)
            #img = imread(filename)
            img = cv2.imread(filename)
            if len(img.shape)>2 and img.shape[2] ==4:
                img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            new_shape = (img.shape[0] * img.shape[1] * 3)
            img_as_array = img[:, :, :3].reshape(new_shape)
            height, width, chan = img.shape
            assert chan == 3
            X.append(img_as_array)
            y.append(class_index)
            # useful_image_count += 1
    # print("processed {}, used {}".format(processed_image_count,useful_image_count))

    X = np.array(X).astype(np.float32)
    print('y.shape:', len(y))
    y = np.array(y)

    return X, y, tags

def dataset_list(base_dir, n, symbol_list):
    print("trad. base_dir : {}, n : {}".format(base_dir, n))
    X = []
    y = []
    f = open(symbol_list)
    s_list=[]
    while True:
        line = f.readline()
        s_list.append(line.strip("\n"))
        if not line:
            break
    f.close()
    print('symbol_list:',s_list)
        

    
    for symbol in s_list:
        base_dir_ = base_dir%symbol
        d = defaultdict(list)
        for root, subdirs, files in os.walk(base_dir_):
            for filename in files:
                file_path = os.path.join(root, filename)
                assert file_path.startswith(base_dir_)
                suffix = file_path[len(base_dir_):]
                suffix = suffix.lstrip("\\")
                label = suffix.split("\\")[0]
                d[label].append(file_path)

        tags = sorted(d.keys())
        # print("classes : {}".format(tags))
        # useful_image_count = 0


        for class_index, class_name in enumerate(tags):
            filenames = d[class_name]
            for filename in filenames:
                #img = scipy.misc.imread(filename)
                #img = imread(filename)
                img = cv2.imread(filename)
                if len(img.shape)>2 and img.shape[2] ==4:
                    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
                new_shape = (img.shape[0] * img.shape[1] * 3)
                img_as_array = img[:, :, :3].reshape(new_shape)
                height, width, chan = img.shape
                assert chan == 3
                X.append(img_as_array)
                y.append(class_index)
                # useful_image_count += 1
        # print("processed {}, used {}".format(processed_image_count,useful_image_count))

    X = np.array(X).astype(np.float32)
    print('y.shape:', len(y))
    y = np.array(y)

    return X, y, tags