# -*- coding=utf-8 -*- 
# github: night_walkiner
# csdn: 潘迪仔

import hashlib      # 导入加密库
from django3_1.settings import SECRET_KEY       # 导入django内置的盐

def md5(data_string):

    # 加密盐---就是用来辅助加密的，可以说是给密文再加一个随机数吧？
    # 有两种方法，一种是自定义的，一种是使用django内置的

    # salt = "xxxx"                       # 自定义的盐---1

    obj = hashlib.md5()             # 实例化 MD5 加密类

    # obj.update(salt.encode('utf-8'))    # 自定义的盐---2
    # 如果是使用 django 默认的盐，在项目的 setting.py 文件中的 SECRET_KEY 变量就是django自己的盐
    # 我们可以直接使用。
    obj.update(SECRET_KEY.encode('utf-8'))      # 给盐加密
    obj.update(data_string.encode('utf-8'))     # 给传入的字符串加密

    return obj.hexdigest()

