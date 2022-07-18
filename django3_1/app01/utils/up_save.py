import os

# path = os.path()


class UpSave(object):
    """
    写入视频到 videos 中，以供姿态估计算法调用
    """
    def __init__(self, file_object, path_folder):

        self.init_path = os.getcwd()
        self.file_object = file_object

        path = r'D:\\Code\\django3_1\\{}'.format(path_folder)

        if not os.path.exists('D:/Code/django3_1/{}'.format(path_folder)):
            os.mkdir(path)
        os.chdir("D:/Code/django3_1/{}/".format(path_folder))

        f = open(self.file_object.name, mode='wb')
        for chunk in self.file_object.chunks():
            f.write(chunk)
        f.close()

        os.chdir(self.init_path)



