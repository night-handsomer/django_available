# -*- coding=utf-8 -*-
# 作者: night_walkiner
# csdn: 潘迪仔


import os.path

import cv2

from django.shortcuts import render
from app01.utils import sports_analysis
from app01 import models
from app01.utils.sports_analysis import *
from app01.utils.sports_analysis import SportsAnalysis


def get_kpt(request):
    """
    # 业务流程
        # (1)读取输入动作的姿态估计的结果___一般命名为test.npz。

        # (2)输入和标准的帧数不等，因此要进行对准匹配。

        # (3)计算输入的和标准的姿态的骨骼相似度。

        # (4)求取相似度最低的三帧图片，以下还要分出来。
            # 1)首先要找出最小的，并且pop出去，此时list长度为 len(list) - 1
            # 2)循环上面的过程两次，当然这个可以自己定义

        # (5)输出上面的三个图片，然后传入到前台显示
    """
    name = request.POST.get("sports_name")
    # 当然这里也可以封装一个函数，生成对应的类型运动
    # 看需要
    img_path_list = []
    static_path = 'app01/static/img/esti_analysis/{}'

    if name == "太极":
        # 创建保存错误姿态帧图的文件夹
        static_path = static_path.format('taiji')
        # print(static_path)
        if not os.path.exists(static_path):
            os.mkdir(static_path)

        # 动作分析
        analysis = SportsAnalysis(estimate_kpt='t_data.npz', std_kpt='std_taiji.npz', output_path="output.avi", min_num=4)
        img, scores = analysis.min_fr()
        img_length = len(img)

        # 写入图片
        if write_img(img, static_path, img_length):

            init = static_path
            for i in range(img_length):
                static_path = init
                static_path = os.path.join(static_path, "err_img{}.jpg".format(i + 1))
                r_path = split_words(static_path)
                img_path_list.append(r_path)

    elif name == "篮球":
    # 简单解释下新动作部署的流程
        # (1)首先必须准备好，一个标准的篮球动作进行姿态序列估计，并且保存；自己输入的篮球上篮视频，也要进行姿态估计。
        # (2)------------------------------------------同上
        pass
    elif name == "其他运动":
        # 同上
        pass


    # 前台传参
    context = {
        'name': '',
        'sports': img_path_list

    }

    return render(request, "sports_analysis.html", context)

