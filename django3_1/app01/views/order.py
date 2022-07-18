# -*- coding=utf-8 -*- 
# github: night_walkiner
# csdn: 潘迪仔
import json

import random
from app01 import models
from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app01.utils.pagination import Pagination
from app01.utils.bootstrap import BootStrapModelForm

class OrderModelForm(BootStrapModelForm):

    class Meta:
        model = models.Order
        fields = "__all__"
        # 如果想要排除某个字段，就可以使用这个变量,我们排除掉 oid，因为我们要随机生成，
        # admin 字段我们也改动一下，让这个订单的负责人默认是当前登录的用户
        exclude = ["oid", "admin"]


def order_list(request):
    # 数据库中取订单数据
    queryset = models.Order.objects.all().order_by('-id')

    # 添加分页功能
    multi_page = Pagination(request, queryset)
    # 生成相应的 html 标签
    form = OrderModelForm()

    context = {
        "form": form,
        "multi_page": multi_page.page_queryset,     # 页面数据
        "page_string": multi_page.html,             # 生成分页的标签
    }
    return render(request, "order_list.html", context)



@csrf_exempt
def order_add(request):

    ret = {
        "code": 1000,
        "status": True
    }
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        # 添加 oid 的值
        # datetime.now() 是获取当前时间, .strftime() 方法就是将时间转化为字符串
        oid = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))

        # 给 form 的某个字段加值, 就是 form.instance.字段名
        form.instance.oid = oid

        # 负责人 admin, 在 session 的时候，我们有设置过用户登录的 id
        form.instance.admin_id = request.session["info"]["id"]
        form.save()

        return JsonResponse(ret)

    ret["code"] = 1002
    ret["status"] = False
    ret["error"] = form.errors

    return JsonResponse(ret)


# 删除
def order_delete(request):
    # 获取前端的数据
    uid = request.GET.get("uid")

    # 验证当前数据是否存在
    if not models.Order.objects.filter(pk=uid).exists():
        ret = {
            "code": 1001,
            "status": False,
            "error": "所删除数据不存在"
        }
        return JsonResponse(ret)
    # 删除对应的数据
    models.Order.objects.filter(pk=uid).delete()
    ret = {
        "code": 1000,
        "status": True
    }

    return JsonResponse(ret)

def order_edit(request):

    uid = request.GET.get("uid")

    """
        从数据库中取数据，返回的类型：
        对象  (1) row_object = models.Order.objects.filter(pk=uid).first(), 
                # row_object 是一个对象。取数据的话，比如 title 属性。
                # 获取数据可以 row_object.title 就是点属性的方法。
                # 但是这种查询方式是返回对象，无法以 Json 格式为序列化数据返回。
                
        字典  (2) row_list = models.Order.objects.filter(pk=uid).values("title", "price", "status").first()
                # 还有一种方法。但其实也可以是使用 .values() 方法，
                # 这样子返回的是一个字典，即 row_list = {'title': '电视', 'price': 1231232, 'status': 2}
            
    对象查询集 (3) row = models.Order.objects.all() 
                # 返回的是一个对象查询集合, 即 <QuerySet [<Order: Order object (4)>, ...], 每一个对象都是一条数据
                # 可以通过 row[0].title 来第一条数据的属性值
            
    字典查询集 (4) row = models.Order.objects.all().values("title", "price")
                # 这里我们指定了特定的值，那么返回的就是一个字典查询集合，即 [{}, {}, ...], 每一个 {} 是一条数据。
                # 事实上输出例如：<QuerySet [{'title': '手机', 'price': 12312}, {'title': '1231', 'price': 2131}, ...]>
                
        元组  (5) row = models.Order.objects.all().values_list("title", "price")
                # 这里返回的是元组查询集。就是 [(), (), ...] , 每一个 () 是一条数据, 
                # 里面元素的个数取决于我们给的 values_list("a", "b", "c", ...)  括号里面的字段个数。 
                # 比如我们只给了两个属性，那么就是这样的 <QuerySet [('手机', 12312), ('1231', 2131), ...]
    """

    # 这里我们用上面的第 (2) 种方法
    row_list = models.Order.objects.filter(pk=uid).values("title", "price", "status").first()
    if not row_list:

        ret = {
            "code": 1002,
            "status": False
        }

        return JsonResponse(ret)
    # 查询成功的话，返回相应的数据
    ret = {
        "code": 1000,
        "status": True,
        "data": row_list
    }
    return JsonResponse(ret)


# 编辑的保存
@csrf_exempt
def order_save(request):
    # 注意区分，我们索引 id 的请求是 GET 请求
    uid = request.GET.get("uid")
    row_object = models.Order.objects.filter(pk=uid).first()
    # 判断当前的数据是否存在
    if not row_object:
        ret = {
            "code": 1003,
            "err_msg": "当前修改的数据不存在"
        }
        return JsonResponse(ret)

    form = OrderModelForm(data=request.POST, instance=row_object)

    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    # 如果输入为空的，要返回的错误信息
    ret = {
        "code": 1003,
        "error": form.errors
    }
    return JsonResponse(ret)


