# -*- coding=utf-8 -*- 
# github: night_walkiner
# csdn: 潘迪仔


from django import forms
from app01 import models
from django.shortcuts import render, redirect, HttpResponse

from app01.utils.encrypt import md5
from app01.utils.check_words import check_code
from app01.utils.bootstrap import BootStrapForm

class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput,
        required=True
    )
    verify = forms.CharField(
        label="验证码",
        widget=forms.TextInput,
        required=True
    )

    # 钩子方法---来判断获得密码的值
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        # 对密码进行 md5() 加密
        return md5(pwd)


def admin_login(request):
    """登录"""
    if request.method == "GET":
        form = LoginForm()
        context = {
            "form": form,
        }
        return render(request, 'login.html', context)

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # cleaned_data 就是获得的 post 数据。比如结果是 {'username': '123', 'password': '123', 'verify': xxxx}

        user_input_code = form.cleaned_data.pop("verify")
        # request.session.get("img_code", "") 如果 img_code 没有，那么就默认为空
        img_code = request.session.get("img_code", "")
        # .upper() 是可以将字符串里面全部都大写
        if img_code.upper() != user_input_code.upper():
            form.add_error("verify", "验证码输入错误")
            return render(request, 'login.html', {'form': form})


        admin_info = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_info:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {'form': form})

        # 用户密码校验成功后，网站生成随机字符串；写到用户浏览器的 cookie 中；再写入到 session 中。
        # admin_info 是从数据库中取出的。
        request.session["info"] = {"id": admin_info.id, "name": admin_info.username}
        # 设置 7 天免登录
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect('/admin/list/')

    return render(request, 'login.html', {"form": form})



# 注销
def admin_logout(request):
    """注销函数"""
    # 清楚当前用户的 session 信息
    request.session.clear()

    # 重定向回登录页面
    return redirect('/login/')


def check_words(request):
    # 验证码的生成
    # (1) 导入图片验证码插件。
    img, code_words = check_code()

    # 验证码的校验。每个用户在登录时候，肯定是对应不同的验证码
    # 我们利用 session 每个用户对应不同的信息，然后将各自的验证码放入到 session 的新增字段 img_code 中。
    request.session['img_code'] = code_words
    # request.session.set_expiry(x) 是用来设置验证码有效时间为 x 秒的
    request.session.set_expiry(60)


    # (2) 写入内存(Python3)
    # 其实这一步我们是要把 img 写入辅存（磁盘），然后再从辅存取出使用的。但是我们知道cpu、内存、辅存的三者的写入写出关系，
    # 因此为了加快这个调用逻辑，我们可以将图片对象暂时存在内存中。那么具体的操作如下：
    from io import BytesIO  # 这是操作内存的一个工具
    # 实例化内存流对象
    stream = BytesIO()
    # (3) 使用 img.save() 存在内存流中。这里可以理解为，保存了 stream.png 图片，只是存在内存而已。
    img.save(stream, 'png')
    # (4) stream.getvalue() 就是取出保存在内存中的图片验证码。其名称就是 stream 了



    return HttpResponse(stream.getvalue())



