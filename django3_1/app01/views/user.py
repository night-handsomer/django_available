from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import UserModelForm


"""用户管理"""


# 用户信息列表
def user_list(request):
    # （1）获取用户表的数据
    queryset = models.UserInfo.objects.all()
    total_count = models.UserInfo.objects.all().count()
    # page_object = Pagination(request, queryset, total_count)
    page_object = Pagination(request, queryset)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, "user_list.html", context)


# 添加用户---原始
def user_add(request):
    """原始法"""
    if request.method == "GET":
        queryset = models.Department.objects.all()
        # 如果render的后面传参太长可以使用下面的方法，即将参数封装成字典
        context = {
            'gender_list': models.UserInfo.gender_chioce,
            'queryset': queryset,
        }
        return render(request, "user_add.html", context)

    # 获取用户提交的数据
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")
    account = request.POST.get("account")
    ctime = request.POST.get("ctime")
    gender_id = request.POST.get("gd")
    depart_id = request.POST.get("dp")

    # 写入数据库
    models.UserInfo.objects.create(name=user, password=pwd, age=age, account=account, create_time=ctime,
                                   gender=gender_id, depart_id=depart_id)

    return redirect("/user/list/")


def user_model_form_add(request):
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, "user_model_form_add.html", {"form": form})

    # 用户POST提交数据，数据校验。
    form = UserModelForm(data=request.POST)  # request.POST是取到fields里面所有字段的值
    # 使用form.is_valid()来对提交的数据进行校验
    if form.is_valid():
        # print(form.cleaned_data)  # form.cleaned_data是校验成功后，取到的所有信息
        # form.save()是modelform给的方法，能够自动将提交的数据保存到数据库。
        # 就相当于执行了models.UserInfo.objects.create()的orm操作语句。
        form.save()
        return redirect('/user/list/')
    else:
        # 校验失败，则显示错误信息
        # form.errors里面封装了每一个字段的错误信息，而且包含其错误类型。错误类型是一个列表[错误1， 错误2， 。。。]，
        # 当某个字段出现错误k时，则会输出对应的错误，我们可以简单的认为就是错误1，
        # 因此，我们只需要取第一个就可以了，也就是在前端写为{{ form.errors.0 }}
        return render(request, "user_model_form_add.html", {"form": form})


# 编辑用户
def user_edit(request, nid):
    if request.method == "GET":
        # （1）首先还是要和先前的基础法一样，
        # 通过models.UserInfo.objects.filter(id=nid).first()来取到数据库对应id的数据
        row_object = models.UserInfo.objects.filter(id=nid).first()
        # （2）在第一步中返回的是一个数据对象row_object，然后我们按照步骤，
        # 将UserModelForm实例化对象，同时把row_object赋给该类的instance属性，
        # 那么框架就会自动传回要编辑的那行数据
        form = UserModelForm(instance=row_object)
        return render(request, "user_edit.html", {"form": form})

    # POST请求，对提交的数据进行校验
    # （1）首先是取到要更新的那行数据的ID，然后获取编辑后的数据
    row_object = models.UserInfo.objects.filter(id=nid).first()  # 获取id
    # 实例化form后，需要设置两个属性，前者data是获取的数据的属性，后者instance是要更新的那行数据
    form = UserModelForm(data=request.POST, instance=row_object)
    # （2）数据校验
    if form.is_valid():
        # 有了data和instance的属性后（后者必须设置，如果只设置前者那么系统只会是添加一条数据），
        # form.save()才能更新要求更新的那行数据。
        form.instance.password = 123
        form.save()
        return redirect("/user/list/")
    else:
        return render(request, "user_edit.html", {"form": form})


# 用户删除
def user_delete(request, nid):
    # 先获取用户点击的那行数据
    models.UserInfo.objects.filter(id=nid).delete()
    # 重定向
    return redirect("/user/list/")

