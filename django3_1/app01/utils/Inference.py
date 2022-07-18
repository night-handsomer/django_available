import os
# 设置图片类型的字典，用于判断是否为图片
imgType = ['jpg', 'bmp', 'png', 'jpeg', 'tif', 'rgb']


class UpInference(object):
    """执行姿态估计模块的命令"""

    def __init__(self, file_name, imgType=imgType):

        self.file_name = file_name.split('.')[-1]
        self.imgType_list = imgType

        # 如果是视频，就执行视频的语句
        if self.file_name in self.imgType_list:
            # 下面是对图片进行估计的命令
            os.system("python demo/demo.py --image videos/{} --showFps --write".format(file_name))
        else:
            # 下面是对视频进行估计的命令
            os.system("python demo/demo.py --video videos/{} --showFps --write".format(file_name))

