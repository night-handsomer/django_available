# 导入文件

from django import forms
from django.shortcuts import render, redirect, HttpResponse
from django.core.exceptions import ValidationError


from app01 import models
from app01.utils.encrypt import md5
from app01.utils.search import SearchingBox
from app01.utils.pagination import Pagination
from app01.utils.bootstrap import BootStrapModelForm


def admin_list(request):
    """管理员列表"""
    # 验证凭证是否存在
    # 用户发送请求，获取 cookie 随机字符串，拿着随机字符串看看 session 中有没有。
    # 如果有的话，说明用户登录了；否则就是没有登录
    # Django 内置了这个方法，我们只需要执行 request.session.get('info') 就可以知道了。

    # info = request.session.get('info')
    # # 如果没登录，那么 info 为 None，即重定向回登录页面
    # if not info:
    #     return redirect('/admin/login/')






    # 搜索功能
    dict = SearchingBox(request, "username")
    dict_data = dict.data_dict          # 获取数据字典

    quesryset = models.Admin.objects.filter(**dict_data)        # 查询集
    # 分页功能
    page_obj = Pagination(request, quesryset)

    context = {
        "quesryset": page_obj.page_queryset,
        "search_data": dict.search_data,        # 设置留置值，就是查询之后，搜索框依然有搜索的那个关键字
        "page_string": page_obj.html()
    }

    return render(request, "admin_list.html", context)

# 通用方法
class AdminModelForm(BootStrapModelForm):
    # 如果数据库中没有的字段，我们可以通过下面的这个语句来添加该字段，相当于临时添加的
    # 如果密码在填写的时候想要是加密方式的，就要传参 widget=forms.PasswordInput(render_value=True)
    # render_value=True 的作用就是，如果密码错误了，是不是清空所有输入(相当于留置)，如果为True就是不清空，否则就是清空
    confirm_pwd = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ["username", "password", "confirm_pwd"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    # 对密码进行加密
    def clean_password(self):
        # 获取用户提交的密码
        pwd = self.cleaned_data.get("password")


        # 返回用户提交的密码，要注意返回的 pwd 是什么，那么clean_confirm_pwd()函数里的密码拿到的就是什么（是密码的，不是确认密码的）
        # 然后我们对获得的密码进行md5加密
        return md5(pwd)

    # 钩子方法，其实就是人家forms里面内置的函数，我们重写而已。
    def clean_confirm_pwd(self):
        # 获取密码字段
        pwd = self.cleaned_data.get("password")
        # 获取确认密码的字段
        confirm = md5(self.cleaned_data.get("confirm_pwd"))

        # 比较两次密码的一致性(这里是密文的比较)
        if pwd != confirm:
            raise ValidationError("密码不一致")
        # 返回确认密码的值，显然确认密码肯定是正确了才能返回的，这也是最终存在数据库的值
        # 也就是说，在这个内置的钩子函数中，返回的是什么，那么什么就存在数据库中。
        # 因为使用的是密文，因此存入数据库的也是密文来的
        return confirm


# 添加管理员
def admin_add(request):

    title = "新建管理员"
    if request.method == "GET":
        form = AdminModelForm()
        print(form)
        return render(request, "change.html", {"title": title, "form": form})

    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)        # form.cleaned_data是验证通过后，得到的提交的所有数据
        form.save()
        return redirect('/admin/list')

    return render(request, "change.html", {"title": title, "form": form})





# 编辑的通用类---因为我们想编辑功能只能是对用户名做更改，因此我们只需要渲染出用户名的就行了
class AdminEditModelForm(BootStrapModelForm):

    class Meta:
        model = models.Admin
        fields = ["username"]


# 编辑函数
def admin_edit(request, nid):

    # 首先要判断获取的 nid 是不是合法的，也就是存不存在
    # 如果存在，那么返回就是这个id对应的对象，不存在返回值就是None
    row_obj = models.Admin.objects.filter(id=nid).first()
    # 如果不存在的话
    if not row_obj:
        # 就重定向回该页面，当然也可以自定义一个错误页面
        return redirect('/admin/list')

    title = "编辑管理员"
    if request.method == "GET":
        # instance 是显示编辑框的占位符，就是原来的默认值。
        # 比如原来用户名是梁旭，那么修改时候的占位符就是梁旭。
        form = AdminEditModelForm(instance=row_obj)

        return render(request, "change.html", {"title": title, "form": form})

    # 这里实例化后，为什么还要带上instance，这是因为如果不带这个的话，就会出现用户名重复的情况
    # 因此需要带上，来覆盖掉原来要修改的那个值。
    form = AdminEditModelForm(data=request.POST, instance=row_obj)
    # print(row_obj.username)

    # 校验数据
    if form.is_valid():
        form.save()

        return redirect('/admin/list')
    # 如果校验不成功，那么依然停在编辑页面
    return render(request, "change.html", {"title": title, "form": form})




# 删除函数
def admin_delete(request, nid):

    # 删除对应id的数据
    models.Admin.objects.filter(id=nid).delete()
    # 重定向回管理员列表
    return redirect('/admin/list/')


# 重置密码类
class AdminResetModelForm(BootStrapModelForm):

    confirm_pwd = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:

        model = models.Admin
        fields = ['password', 'confirm_pwd']
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

# 对密码进行加密---因为修改密码，所以一样要定义钩子方法来对输入密码进行验证
    def clean_password(self):
        # 获取用户提交的密码
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)

        # 去数据库校验，修改的密码和原先的密码是否相同，如果相同则报错
        # self.instance.pk 就是我们要修改的那行数据的id。比如想要对用户 梁旭(id=1) 的密码进行修改，
        # 那么self.instance.pk = id = 1（就是nid）
        # password=md5_pwd 其实就是查询的另一个条件，即梁旭原来存在数据库的密码。
        # 因此下面语句就是查询符合给定的id，密码的数据，显然如果该数据存在，说明原始密码与给定的密码是相同的
        # 【注意，此时md5_pwd是用户新改的密码，如果新改的密码在查询时不匹配，exist都是None的】
        exist = models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exist:
            raise ValidationError("新密码不能与旧密码一致")
        return md5_pwd

    # 钩子方法，其实就是人家forms里面内置的函数，我们重写而已。
    def clean_confirm_pwd(self):
        # 获取密码字段
        pwd = self.cleaned_data.get("password")
        # 获取确认密码的字段
        confirm = md5(self.cleaned_data.get("confirm_pwd"))

        # 比较两次密码的一致性(这里是密文的比较)
        if pwd != confirm:
            raise ValidationError("密码不一致")
        # 返回确认密码的值，显然确认密码肯定是正确了才能返回的，这也是最终存在数据库的值
        # 也就是说，在这个内置的钩子函数中，返回的是什么，那么什么就存在数据库中。
        # 因为使用的是密文，因此存入数据库的也是密文来的
        return confirm

# 重置密码函数
def admin_reset(request, nid):

    title = '重置密码'
    # 判断传回的 id 是不是合法的
    row_obj = models.Admin.objects.filter(id=nid).first()
    if not row_obj:
        return redirect('/admin/list/')


    if request.method == "GET":
        # 前端渲染
        form = AdminResetModelForm()
        # 返回重置密码页面
        return render(request, 'change.html', {"form": form, "title": title})

    form = AdminResetModelForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')

    return render(request, 'change.html', {"form": form, "title": title})










