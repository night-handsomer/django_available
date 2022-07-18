import os

from app01.utils.up_save import UpSave
from app01.utils.Inference import UpInference
from django.shortcuts import render, HttpResponse, redirect


# 上传估计测试
def up_test(request):

    if request.method == "GET":
        return render(request, "up_test.html")
    '''
        # 请求体中的数据
        print(request.POST)
        # 请求发来的文件，下面是一个文件对象，包含了文件内容
        # <MultiValueDict: {'avatar': [<TemporaryUploadedFile: video.mp4 (video/mp4)>]}>
        print(request.FILES)
    '''
    # 综上， 我们想要获取文件时，就可以根据下面的方法来获取了，avatar是前端文件上传时我们给的值。
    # 要注意file_object里面包含了我们的文件内容，因此想要获取内容就需要读取上传的内容
    file_object = request.FILES.get("avatar")
    # 执行
    up_save = UpSave(file_object, "videos")

    if os.path.exists("D:/Code/django3_1/videos/{}".format(file_object.name)):
        exec = UpInference(file_name=file_object.name)
        return HttpResponse("提交成功")


















    """
    # 读取方法，文件是一块一块的上传的（可以这么理解）。
    init_path = os.getcwd()  # 获取当前的系统路径
    # 设置一个我们指定的路径来存储文件
    path = r'D:\\Code\\django3_1\\videos'
    # 利用os.path.exists()来看看指定的路径有没有这个文件夹，没有就创建一个
    if not os.path.exists('D:/Code/django3_1/videos'):
        os.mkdir(path)
    # 创建好了目标的文件夹后，我们就要切换工作路径了，os.chdir()能帮我们实现，注意最后一个是有/的
    os.chdir("D:/Code/django3_1/videos/")
    # 我们转换了工作路径之后，那么在这个时候执行的open()函数写入的文件就是放在指定的path下面了
    f = open(file_object.name, mode='wb')
    for chunk in file_object.chunks():
        f.write(chunk)
    f.close()
    # print("H:/Django/code/django3_1/videos/{}".format(file_object.name))
    # 转换回原来的工作目录
    os.chdir(init_path)
    # 判断上传的文件是否存在
    # try:
    if os.path.exists("D:/Code/django3_1/videos/{}".format(file_object.name)):
        # print(file_object.name)
        # 执行姿态估计命令
        exec = UP_Inference(file_name=file_object.name)
        return HttpResponse("提交成功")
    else:
        return HttpResponse("提交失败")
    """


