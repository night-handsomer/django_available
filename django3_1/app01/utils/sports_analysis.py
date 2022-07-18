# -*- coding=utf-8 -*-
# 作者: night_walkiner
# csdn: 潘迪仔

import os
import cv2
import numpy
import torch
import random
import numpy as np


def Save_test(input, filename):
    """
    用来将numpy的数据类型，保存为 txt 文件的
    :param input:
    :param filename:
    :return:
    """
    k = []
    file_name = "{}.txt".format(filename)
    for i in input:
        k = i
    if not os.path.exists(file_name):
        np.savetxt(file_name, k, fmt="%f", delimiter=",")
        return print("save_ok")
    else:
        data = np.loadtxt(file_name, dtype=np.float32, delimiter=",")

        return data


def get_list(num, input):
    """
    获得左右关键点的坐标
    :param num:
    :param input:
    :return:
    """
    list = []
    if num == 5:
        for i in range(num, 17, 2):
            list.append(input[i])

    elif num == 6:
        for i in range(num, 18, 2):
            list.append(input[i])
    else:
        raise TypeError

    return list


# scalar
def sca(input1, input2):
    """
    计算两个向量的余弦相似度所需要的 向量点积和向量模的积
    :param input1:
    :param input2:
    :return:
    """
    # 求两个向量的点乘
    v = np.dot(input1, input2)
    # 求两个向量的模并且相乘
    s1 = np.sqrt(np.square(input1[0]) + np.square(input1[1]))
    s2 = np.sqrt(np.square(input2[0]) + np.square(input2[1]))
    s = s1 * s2
    result = v / s
    return result


def rev(list):
    """
    翻转列表
    :param list:
    :return:
    """

    return [ele for ele in reversed(list)]


def skeleton_vector(input):
    """
    获取骨骼向量
    :param input:
    :return:
    """
    l = []
    r = rev(input)

    for i in range(len(r)):

        if not i == len(r)-1:
            minus = r[i] - r[i+1]
            l.append(minus)

    minus = rev(l)
    list = minus[0:2] + minus[-2:]
    return list


def get_ske_mean(in_left, in_right, std_left, std_right, ran=4):
    """
        计算并且返回最终的余弦相似度的均值，
    :param in_left:
    :param in_right:
    :param std_left:
    :param std_right:
    :param ran:
    :return:
    """


    left = []
    right = []

    # 输入的左右的骨骼向量
    left_ske = skeleton_vector(in_left)
    right_ske = skeleton_vector(in_right)

    left_std = skeleton_vector(std_left)
    right_std = skeleton_vector(std_right)

    for i in range(ran):

        l_res = sca(left_ske[i], left_std[i])
        r_res = sca(right_ske[i], right_std[i])
        left.append(l_res)
        right.append(r_res)

    total = left + right
    sum = 0
    for i in range(len(total)):
        sum += total[i]

    mean = sum / len(total)

    return mean


"""
    针对视频的
"""


# 添加每一帧的关键点坐标
def list_add(list, input):

    in_tensor = torch.tensor(input)
    l = list
    l.append(in_tensor)

    return l


# 在得出结果后，将姿态关键点序列进行匹配
def mapped(min_len, data):

    m = len(data) - min_len
    if m > 0:
        initial = random.randint(0, m)
        n = min_len + initial
        data2 = data[initial:n, :, :]
        return data2

    else:
        return data


# 得到每一帧序列的余弦相似度
def get_ske_analyse(input, std):

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

    # 计算平均分
    l_sum = 0
    for i in range(len(list)):
        l_sum += list[i]
    total_scores = l_sum / len(list)
    return list, total_scores


"""
    针对视频的姿态分析
"""
# hrnet的关键点标注的函数，需要的前置参数---------（1）
SKELETON = [
    [1, 3], [1, 0], [2, 4], [2, 0], [0, 5], [0, 6], [5, 7], [7, 9], [6, 8], [8, 10], [5, 11], [6, 12], [11, 12], [11, 13], [13, 15], [12, 14], [14, 16]
]


CocoColors = [[255, 0, 0], [255, 85, 0], [255, 170, 0], [255, 255, 0], [170, 255, 0], [85, 255, 0], [0, 255, 0],
              [0, 255, 85], [0, 255, 170], [0, 255, 255], [0, 170, 255], [0, 85, 255], [0, 0, 255], [85, 0, 255],
              [170, 0, 255], [255, 0, 255], [255, 0, 170], [255, 0, 85]]

NUM_KPTS = 17


# hrnet的关键点标注的函数，直接取用的---------（2）
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


# 输出不标准的姿态----（第一种写法）
def draw_min(min_frame, video_path, min_frame_kpt):
    """
    输出不标准的那个动作

    :param min_frame:
    :param video_path:
    :param min_frame_kpt:
    :return:
    """
    sum = 0
    video = cv2.VideoCapture(video_path)
    while True:

        ret, img = video.read()
        sum += 1
        if sum == min_frame:
            if min_frame_kpt.shape == (17, 2):
                min_frame_kpt.resize(1, 17, 2)

            for kpt in min_frame_kpt:
                draw_pose(kpt, img)
            break

    return img


# 输出不标准的姿态---（第2种方法）---推荐~~~

def draw_min_in_output(min_frame, output_path):

    sum = 0
    video = cv2.VideoCapture(output_path)

    while True:

        ret, img = video.read()

        if sum == min_frame:
            show = img
            break
        sum += 1

    return show


# 找出最小的三帧
def find_tri_min(smi_list, min_num=3):
    l = []
    for i in range(min_num):

        min_idx = np.argmin(smi_list)
        l.append(min_idx)
        smi_list = np.delete(smi_list, min_idx)

    return l


# 工具类的联合
class SportsAnalysis(object):

    def __init__(self, estimate_kpt, std_kpt, output_path, min_num=3):
        """

        :param estimate_kpt: 姿态估计的关节点结果存放的位置，格式为npz
        :param std_kpt:     标准姿态的关节点结果存放位置，格式同上
        :param output_path: 使用姿态估计算法渲染后的输出视频，给出路径即可
        :param min_num(option):     设置想要找出的相似最小的帧数，默认为3
        """
        self.estimate_kpt = estimate_kpt
        self.std_kpt = std_kpt
        self.output_path = output_path

        # (1)读取输入的和标准的关键点---读取npz格式的文件，并且生成相应的张量
        input = np.load(self.estimate_kpt)
        std = np.load(self.std_kpt)
        self.input = input['arr_0']
        self.std = std['arr_0']

        # (2)匹配帧数
        self.min_length = min(len(self.input), len(self.std))
        self.map_input = mapped(self.min_length, self.input)
        self.map_std = mapped(self.min_length, self.std)

        # (3)计算输入的和标准的骨骼相似度
        self.list, self.scores = get_ske_analyse(input=self.map_input, std=self.map_std)

        # (4)找出相似度最小的 min_num 帧的索引
        self.min_num = min_num
        self.l3 = find_tri_min(self.list, self.min_num)

    # (5)输出最小的三帧
    def min_fr(self):

        img = []

        for i in range(len(self.l3)):
            show = draw_min_in_output(self.l3[i], self.output_path)
            img.append(show)

        img = np.array(img)
        return img, self.scores

    # 生成前台展示要用的html代码，option~~
    def show_html(self):

        pass


# 写入图片到static文件夹
def write_img(img, init_path, length):
    """
    写入图片到指定文件夹
    :param img: 输入的图片
    :param init_path: 目标文件夹位置
    :param length: 图片的个数，一般img得到的是一个数组，其长度就是帧数（也就是图片的个数）
    :return:
    """
    if len(img)>=1:
        for i in range(length):

            init = init_path
            err_idx = 'err_img{}.jpg'.format(i + 1)
            init = os.path.join(init, err_idx)
            cv2.imwrite(init, img[i])

        return True
    else:

        raise TypeError


# 按需读取所要的字符串
def split_words(input, start_num=-3):

    input_list = input.split("/")[start_num:]
    result = "/".join(input_list)

    return result