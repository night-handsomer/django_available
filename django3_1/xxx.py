"""
class Foo():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


obj = Foo("IT部门")
obj1 = Foo("企划部门")

print(obj)
print(obj1)
"""
import random

import numpy
import torch

'''
fields = ['name', 'password', 'age', 'account', 'create_time', 'gender', 'depart']

def test():

    # for name, field in fields:
    for field in fields:
        # print(name, field)
        str(field)

test()

'''

"""
page_list = []

for i in range(10, 20):
    ele = '<li><a href="?page={}">{}</a></li>'.format(i, i)
    page_list.append(ele)
seq = ("a", "b", "c")

page_string = "__".join(seq)

print(page_list)
print(page_string)
"""

"""
field = {"x": "y"}

field["class"] = "z"
# field = {"handsome": "w"}

print(field)
"""


import imghdr
import os
# 设置图片类型的列表，用于判断是否为图片
imgType_list = {'jpg', 'bmp', 'png', 'jpeg', 'tif', 'rgb'}

# for item in os.listdir(x.jpg):






        #
        # # 如果是视频，就执行视频的语句
        # if video:
        #     os.system("python demo/demo.py --image videos/{} --showFps --write".format(file_name))
        #
        #     # 下面是对视频进行估计的命令
        # else:
        #     # 下面是对图片进行估计的命令
        #     os.system("python demo/demo.py --video videos/{} --showFps --write".format(file_name))




"""
def Save_test(input, filename):

    k = []
    file_name = "{}.txt".format(filename)
    for i in input:
        k = i
    if not os.path.exists(file_name):
        numpy.savetxt(file_name, k, fmt="%f", delimiter=",")
        return print("ok")
    else:
        data = np.loadtxt(file_name, dtype=np.float32, delimiter=",")
        # print(data)
        return data
"""


import numpy as np
import torch.nn as nn

from app01.utils.sports_analysis import Save_test, get_list, get_ske_mean, mapped, skeleton_vector, get_ske_analyse




# 知识增加：
# v = 10
# m = 1
# n = 0
# w = v if m else n       # 这个语句的意思是，如果 m 条件成立，那么执行 v，否则，执行 n
# print(w)






input1 = np.array([[[332.19577, 179.85207],
                   [332.19577, 174.20842],
                   [326.55212, 172.32721],
                   [330.31454, 177.97086],
                   [303.9775, 174.20842],
                   [334.077, 209.95154],
                   [277.64047, 206.1891],
                   [347.2455, 238.1698],
                   [236.25371, 213.71397],
                   [352.88916, 253.21953],
                   [194.86694, 204.30789],
                   [332.19577, 279.55658],
                   [296.45264, 285.20023],
                   [349.1267, 309.65604],
                   [303.9775, 352.924],
                   [352.88916, 364.21133],
                   [305.85873, 409.36053]]])


input2 = np.array([[[171.5562, 179.11772],
                    [173.40364, 173.57541],
                    [166.01387, 173.57541],
                    [169.70876, 177.27028],
                    [143.84457, 173.57541],
                    [175.25108, 208.6768],
                    [117.980385, 206.82936],
                    [186.33574, 238.23587],
                    [75.48922, 212.37169],
                    [193.72551, 253.01541],
                    [32.99805, 201.28703],
                    [171.5562, 277.03217],
                    [136.4548, 286.26935],
                    [188.18318, 310.2861],
                    [143.84457, 349.0824],
                    [191.87807, 363.86194],
                    [145.69202, 406.3531]]])


input3 = np.array([[[171.5562, 179.11772],
                    [173.40364, 173.57541],
                    [166.01387, 173.57541],
                    [169.70876, 177.27028],
                    [143.84457, 173.57541],
                    [175.25108, 208.6768],
                    [117.980385, 206.82936],
                    [186.33574, 238.23587],
                    [75.48922, 212.37169],
                    [193.72551, 253.01541],
                    [32.99805, 201.28703],
                    [171.5562, 277.03217],
                    [136.4548, 286.26935],
                    [188.18318, 310.2861],
                    [143.84457, 349.0824],
                    [191.87807, 363.86194],
                    [145.69202, 406.3531]]])

# Save_test的函数有循环自动给三维数组降维了
data1 = Save_test(input=input1, filename="test_1")
data2 = Save_test(input=input2, filename="test_2")
data3 = Save_test(input=input3, filename="test_3")


t_data1 = torch.tensor(data1)
t_data2 = torch.tensor(data2)
t_data3 = torch.tensor(data3)

# num = 3
# while num > 0:

    # list_add(t_data1)

list = [t_data1, t_data2, t_data3]
# list = [data1, data2, data3]

# data = torch.stack(list, dim=0)
# print(data.size())
# print(type(list))
# print(data)
"""
lt = []
for i in list:
    lt = list_add(lt, i)

data = torch.stack(lt, dim=0)
print(data.size())
print(data)
"""
COCO_KEYPOINT_INDEXES = {
    0: 'nose',
    1: 'left_eye',
    2: 'right_eye',
    3: 'left_ear',
    4: 'right_ear',
    5: 'left_shoulder',
    6: 'right_shoulder',
    7: 'left_elbow',
    8: 'right_elbow',
    9: 'left_wrist',
    10: 'right_wrist',
    11: 'left_hip',
    12: 'right_hip',
    13: 'left_knee',
    14: 'right_knee',
    15: 'left_ankle',
    16: 'right_ankle'
}

COCO_INSTANCE_CATEGORY_NAMES = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
    'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]

SKELETON = [
    [1,3],[1,0],[2,4],[2,0],[0,5],[0,6],[5,7],[7,9],[6,8],[8,10],[5,11],[6,12],[11,12],[11,13],[13,15],[12,14],[14,16]
]

CocoColors = [[255, 0, 0], [255, 85, 0], [255, 170, 0], [255, 255, 0], [170, 255, 0], [85, 255, 0], [0, 255, 0],
              [0, 255, 85], [0, 255, 170], [0, 255, 255], [0, 170, 255], [0, 85, 255], [0, 0, 255], [85, 0, 255],
              [170, 0, 255], [255, 0, 255], [255, 0, 170], [255, 0, 85]]

NUM_KPTS = 17









data_1 = np.load('t_data.npz')
data_2 = np.load('std_taiji.npz')
# data = np.load('kpt.npz')
# print(data.files)
# print(type(data))
# print(len(data["arr_0"]))
# print(data["arr_0"])
# print(type(data["arr_0"]))
d = data_1["arr_0"]
d2 = data_2["arr_0"]
print(d)
# print(len(d))
# print(len(d2))


length = min(len(d), len(d2))
# print(len(d))
# print(len(d2))
# 关键点随机匹配，统一张量
d = mapped(length, d)
d2 = mapped(length, d2)
print("--------------------------------------------------------------\n")

# 分别得到左右关键点。
# input_kpt = d[0:317, 5:17, 0:2]     # 输入
input_kpt = d     # 输入
# std_kpt = d2[0:317, 5:17, 0:2]      # 标准
std_kpt = d2     # 标准
"""
print(input_kpt.shape)
print("--------------------------------------------------------------\n")
print(std_kpt.shape)
# print(type(std_kpt))
ls = input_kpt.shape[0]
list_6 = []

for i in range(input_kpt.shape[0]):

    # 取出姿态序列的第 i 个序列
    l_in = input_kpt[i, :, :]       # 输入的
    l_std = std_kpt[i, :, :]        # 标准的
    # print(l_n.shape)

    # 取出输入的左右姿态的关键点
    left_kpt = get_list(5, l_in)
    right_kpt = get_list(6, l_in)

    # 取出标准的左右姿态关键点
    left_std = get_list(5, l_std)
    right_std = get_list(6, l_std)


    # 计算输入的左右的骨骼向量
    left_vec = skeleton_vector(left_kpt)
    right_vec = skeleton_vector(right_kpt)

    # 计算标准的左右骨骼向量
    left_std_vec = skeleton_vector(left_std)
    right_std_vec = skeleton_vector(right_std)

    # 计算余弦相似度
    mean = get_ske_mean(left_vec, right_vec, left_std_vec, right_std_vec)
    list_6.append(mean)

print(list_6)
print(len(list_6))





def get_ske_vec(input, std):

    list = []

    for i in range(input.shape[0]):

        # 取出姿态序列的第 i 个序列
        l_in = input[i, :, :]  # 输入的
        l_std = std[i, :, :]  # 标准的

        # 取出输入的左右姿态的关键点
        in_left = get_list(5, l_in)
        in_right = get_list(6, l_in)

        # 取出标准的左右姿态关键点
        std_left = get_list(5, l_std)
        std_right = get_list(6, l_std)

        # 计算输入的左右的骨骼向量
        left_vec = skeleton_vector(in_left)
        right_vec = skeleton_vector(in_right)

        # 计算标准的左右骨骼向量
        left_std_vec = skeleton_vector(std_left)
        right_std_vec = skeleton_vector(std_right)

        # 计算余弦相似度
        mean = get_ske_mean(left_vec, right_vec, left_std_vec, right_std_vec)
        list.append(mean)

    return list
"""

import cv2

def draw_pose(keypoints,img):
    """draw the keypoints and the skeletons.
    :params keypoints: the shape should be equal to [17,2]
    :params img:
    """
    # assert keypoints.shape == (NUM_KPTS,2)
    for i in range(len(SKELETON)):
        kpt_a, kpt_b = SKELETON[i][0], SKELETON[i][1]
        x_a, y_a = keypoints[kpt_a][0],keypoints[kpt_a][1]
        x_b, y_b = keypoints[kpt_b][0],keypoints[kpt_b][1]
        cv2.circle(img, (int(x_a), int(y_a)), 6, CocoColors[i], -1)
        cv2.circle(img, (int(x_b), int(y_b)), 6, CocoColors[i], -1)
        cv2.line(img, (int(x_a), int(y_a)), (int(x_b), int(y_b)), CocoColors[i], 2)


list_1, scores = get_ske_analyse(input=input_kpt, std=std_kpt)
# print(list_1)
# print(scores)
min = np.argmin(list_1)
print(min)
output = input_kpt[min, :, :]
# output.resize(1, 17, 2)
# print(output.shape)
# print(output)
# img = cv2.imread('videos/test.jpg')
# for kpt in output:
#     draw_pose(kpt, img)
#
# cv2.imshow('demo', img)
# cv2.waitKey(0)
from video_analysis import draw_min
from app01.utils.sports_analysis import draw_min_in_output
# show = draw_min(min, "videos/taiji2.mp4", output)
show = draw_min_in_output(min, "output.avi")
# print(show)
cv2.imshow('demo_show', show)
cv2.waitKey(0)
# t_data = torch.stack(list, dim=0)
# np.savez("text_1", t_data)
# data = np.load('text_1.npz')
# # print(type(data))
# print(data.files)
# print(data['arr_0'])


# lo = [5, 8, 2, 1, 3, 0, 6, 10]
# print(np.argmin(lo))        # argmin()的函数就是找到最小值的下标，返回。



# print(len(list))
# print(t_data)
# print(t_data.size())
# print(t_data.ndim)
# loss = nn.L1Loss()
# loss = nn.MCELoss()

# data1 = torch.tensor(data1)
# data2 = torch.tensor(data2)

#
# if data1.shape == data2.shape:
#     print("ok")
# print(type(data1))

# result = loss(data1, data2)
# print(result)
#
# e1 = data1[7] - data1[5]
# e2 = data2[7] - data2[5]

# e1 = data1[7] - data1[5]
# e2 = data2[7] - data2[5]
#
# v, s = sca(e1, e2)
# similar = v / s
# print(similar)

# 输入姿态的左右关键点，各自的四组骨骼向量
# in_left = get_list(num=5, input=data1)
# in_right = get_list(num=6, input=data1)

# 标准姿态的左右关键点，各自的四组骨骼向量
# std_left = get_list(num=5, input=data2)
# std_right = get_list(num=6, input=data2)

# 计算余弦相似度
# mean = get_ske_mean(in_left, in_right, std_left, std_right)
# sim = int(mean * 100)
# print("两个姿态的相似程度为：{}%".format(sim))



















# print(e)
# print(e1)
# print(e2)

# x = np.array([3., 4.])
# y = np.array([3., 4.])
# v1 = sca(x, y)
# print(v1)










