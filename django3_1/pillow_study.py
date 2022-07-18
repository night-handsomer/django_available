# -*- coding=utf-8 -*- 
# github: night_walkiner
# csdn: 潘迪仔
# ~~~ 感谢 武sir
# reference: https://www.cnblogs.com/wupeiqi/articles/5812291.html

"""
from PIL import Image

# 使用 Image.new(mode="channel", size=(w, h), color=()) 创建一个图片白板,
#   其中 mode 是选择图片通道的格式是 RGB 还是灰度/黑白;
#   size 是图片的大小, w 是宽, h 是高;
#   color 是什么颜色，比如(255, 255, 255) 是白色
#   由此，下面的意思就是以彩色 RGB 格式，创建一个宽120，高30 的穿白色图片
img = Image.new(mode='RGB', size=(120, 30), color=(255, 255, 255))

img.show()  # 以此可以打开所创建的图片

# 保存图片, 下面的代码就是以 二进制流写的形式保存图片。
# 保存的时候，可以是原来目录没有的文件，也可以是有的
with open('pillow_study.png', 'wb') as f:
    img.save(f, format='png')


# 创建画笔，在图片上画任意的内容, ImageDraw 就是画笔工具了
from PIL import Image, ImageDraw

img = Image.new(mode="RGB", size=(120, 30), color=(255, 255, 255))

# 使用 ImageDraw.Draw(img, mode="") 来创建一个画笔对象。
# img 是基底，我们在这个基底上面画画，其实就是现实的画纸啦
# mode 是颜色通道的意思，不赘述
draw = ImageDraw.Draw(img, mode="RGB")

# (1) 比如我们想要画一个点, 可以使用画笔对象的 point() 方法。
# draw.point([x, y], fill="color")
# 其中第一个参数[x, y]，表示我们涂画点的坐标
# 第二个参数 fill，里面是颜色，比如 fill="red", 也可以是 fill=(255, 255, 255)

# draw.point([100, 20], fill="red")
# draw.point([50, 10], fill=(0, 0, 0))
# img.show()

# (2) 画线
# 使用 draw.line((x0, y0, x1, y1), fill="") 可以实现画线的功能
# 其中第一个参数 (x0, y0, x1, y1) 的意思是 x0, y0 是起始坐标，x1, y1 是终点坐标
# fill 是颜色参数
# draw.line((100, 20, 20, 10), fill="blue")
# img.show()


# 创建画笔，在图片上画任意的内容, ImageDraw 就是画笔工具了
from PIL import Image, ImageDraw

img = Image.new(mode="RGB", size=(1000, 500), color=(255, 255, 255))

# 使用 ImageDraw.Draw(img, mode="") 来创建一个画笔对象。
# img 是基底，我们在这个基底上面画画，其实就是现实的画纸啦
# mode 是颜色通道的意思，不赘述
draw = ImageDraw.Draw(img, mode="RGB")

# (3)画圆
# draw.arc((x0, y0, x1, y1), init_degree, final_degree, fill) 方法就是用来画圆的
# (x0, y0, x1, y1) 其中 x0, y0 是起始点坐标，x1, y1 为结束点坐标;
# init_degree 是开始的角度；final_degree 是结束角度；fill依然是设置颜色
# 这里要说一下，其实这个确切说是画弧，而 init_degree=0, final_degree=360 时，就是一个圆了
# draw.point((100, 100), fill="blue")     # 查看起始点
# draw.point((300, 300), fill="green")    # 查看结束点
# draw.arc((100, 100, 300, 300), 0, 270, fill="red")  # 画一个3/4圆（一个大弧哈哈）
# img.show()





# 创建画笔，在图片上画任意的内容, ImageDraw 就是画笔工具了
from PIL import Image, ImageDraw

img = Image.new(mode="RGB", size=(120, 30), color=(255, 255, 255))

# 使用 ImageDraw.Draw(img, mode="") 来创建一个画笔对象。
# img 是基底，我们在这个基底上面画画，其实就是现实的画纸啦
# mode 是颜色通道的意思，不赘述
draw = ImageDraw.Draw(img, mode="RGB")

# (4) 写文本
# 使用 draw.text([x0, y0], text="", fill="")
# 第一个参数[x0, y0]：表示起始坐标
# 第二个参数text：表示写入内容
# 第三个参数fill：表示颜色
# draw.text([0, 0], 'python', "red")
# img.show()


# 创建画笔，在图片上画任意的内容, ImageDraw 就是画笔工具了, 导入字体工具 ImageFont
from PIL import Image, ImageDraw, ImageFont

img = Image.new(mode="RGB", size=(120, 30), color=(255, 255, 255))

# 使用 ImageDraw.Draw(img, mode="") 来创建一个画笔对象。
# img 是基底，我们在这个基底上面画画，其实就是现实的画纸啦
# mode 是颜色通道的意思，不赘述
draw = ImageDraw.Draw(img, mode="RGB")

# 可以使用 ImageFont.truetype(font="", size= k) 来设置字体的大小和样式
# 那么 font 是具体的字体样式文件，比如 kumo.ttf；
# size 是字体，比如 size=28，默认是10；
# 这样就可以生成一个 font 字体对象
font = ImageFont.truetype("kumo.ttf", 28)
# font = ImageFont.truetype("Monaco.ttf", 28)

# 在应用字体对象的时候，要在 draw.text(.., .., .., font=) 中的 font 设置上，
# 也就是 font=font。其中，上面的 .., 见写文字的讲解。
draw.text([0, 0], "python", "red", font=font)
img.show()

"""


import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def check_code(width=120, height=30, char_length=5, font_file='kumo.ttf', font_size=28):
    code = []
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img, mode='RGB')

    def rndChar():
        """
        生成随机字母
        :return:
        """
        return chr(random.randint(65, 90))

    def rndColor():
        """
        生成随机颜色
        :return:
        """
        return (random.randint(0, 255), random.randint(10, 255), random.randint(64, 255))

    # 写文字
    font = ImageFont.truetype(font_file, font_size)
    for i in range(char_length):
        char = rndChar()
        code.append(char)
        h = random.randint(0, 4)
        draw.text([i * width / char_length, h], char, font=font, fill=rndColor())

    # 写干扰点
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())

    # 写干扰圆圈
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=rndColor())

    # 画干扰线
    for i in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)

        draw.line((x1, y1, x2, y2), fill=rndColor())
    # img.filter() 用来做图像滤波，ImageFilter.EDGE_ENHANCE_MORE 是图像增强的方式，可以深度加强边缘
    # 参考资料：https://wenku.baidu.com/view/b28e261d64ec102de2bd960590c69ec3d5bbdbab.html
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return img, ''.join(code)


# a = 65
# b = 72
#
# c = chr(a)
# d = chr(b)
# print("asc码的映射关系。65 对应的字母 {}，72 对应的字母 {}".format(c, d))

dict = {
    "name": "bobo",
    "age": 12,
    "gender": "男"
}

gender = dict.pop('gender')   # 取出 "gender" 字段的值，然后赋值给 gender 变量，并且在原来的 dict 中删除掉 "gender": "男"

# print(dict)         # 此时的 dict = {'name': 'bobo', 'age': 12}




import math

N0 = 596
K = 8e-3
n = 10
B = 50

N = N0*(math.pow((1+K), n)) - B
print("N的结果是：{}".format(N))

from datetime import datetime
A = datetime.now().strftime("%Y%m%d%H%M%S")
print(A)