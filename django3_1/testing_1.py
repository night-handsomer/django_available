import os

import numpy as np
import cv2
from app01.utils.sports_analysis import SportsAnalysis

analyse = SportsAnalysis(estimate_kpt='t_data.npz', std_kpt='std_taiji.npz', output_path='output.avi')

img, scores = analyse.min_fr()
# print(img.dtype)
print(len(img))

static_path = 'app01/static/img/esti_analysis/taiji'
# init_path = 'app01/static/img/esti_analysis/taiji'
img_length = len(img)

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

"""
if write_img(img, static_path, img_length):
    init = static_path
    for i in range(img_length):
        # 循环一次，
        static_path = init
        static_path = os.path.join(static_path, "err_img{}.jpg".format(i+1))
        print(static_path)
        image_bgr = cv2.imread(static_path)
        cv2.imshow('demo', image_bgr)
        cv2.waitKey(0)
"""


r_path = 'app01/static/img/esti_analysis/taiji'

list_path = r_path.split('/')[-3:]
final_path = "/".join(list_path)
print(final_path)
