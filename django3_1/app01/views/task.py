# -*- coding=utf-8 -*- 
# github: night_walkiner
# csdn: 潘迪仔
import json
from django import forms
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app01 import models
from app01.utils.bootstrap import BootStrapModelForm

class TaskModelForm(BootStrapModelForm):
    class Meta:
        model = models.Task
        fields = "__all__"
        widgets = {
            # model中定义的字段名: forms 中的 css样式
            "detail": forms.TextInput
        }


def task_list(request):
    """任务列表"""
    form = TaskModelForm()

    return render(request, 'task_list.html', {"form": form})





@csrf_exempt
def task_ajax(request):

    # request.GET 可以获取前台传来的参数
    # print(request.GET)

    # request.POST 接收 post 请求来的数据
    print(request.POST)


    # 原始数据为 dict 类型
    dict_data = {"status": True, "data": [11, 22, 33, 44]}
    # # json 化数据
    # json_string = json.dumps(dict_data)
    # return HttpResponse(json_string)
    return JsonResponse(dict_data)


@csrf_exempt
def task_add(request):

    print(request.POST)
    # 接收 ajax 发来的数据
    form = TaskModelForm(data=request.POST)
    # 验证数据有效性
    if form.is_valid():
        # 保存数据
        form.save()
        # 这之后就不是重定向了，可以理解为因为页面没有刷新
        # 所以基于此，我们可以给前端传回一个json
        # 来判断数据是否保存成功
        data = {"status": True}
        return HttpResponse(json.dumps(data))

    # 如果数据无效，就返回错误信息
    data = {"status": False, "errors": form.errors}
    return HttpResponse(json.dumps(data))
