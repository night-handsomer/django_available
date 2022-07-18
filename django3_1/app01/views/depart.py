from django.shortcuts import render, redirect
from app01 import models

"""部门管理"""


# 部门列表
def depart_list(request):
    """部门表"""
    # 1 得到所有的部门信息，返回的是一个查询集合
    queryset = models.Department.objects.all()
    # 2 将返回的查询集合传到相应的html页面中。
    return render(request, "depart_list.html", {"queryset": queryset})
    # return render(request, "test.html", {"queryset": queryset})


# 新建部门
def depart_add(request):
    # （1）首先是GET请求，就获取到添加部门的页面
    if request.method == "GET":
        return render(request, "depart_add.html")

    # （2）用户会在添加页面进行添加，那么是POST请求，因此肯定是request.POST.get()
    title = request.POST.get("title")
    models.Department.objects.create(title=title)

    return redirect('/depart/list/')


# 删除部门
def depart_delete(request):
    # （1）首先获取要删除的部门的id，因为是基于url的获取，因而是使用request.GET.get()方法。
    nid = request.GET.get("nid")
    models.Department.objects.filter(id=nid).delete()
    return redirect("/depart/list/")


# 编辑部门
def depart_edit(request, nid):
    # （1）首先是要获取要编辑的部门的id
    init_title = models.Department.objects.filter(id=nid).first()
    # print(title)
    # （2）转到新页面进行编辑
    if request.method == "GET":
        return render(request, "depart_edit.html", {"init_title": init_title})

    edit_title = request.POST.get("title")
    models.Department.objects.filter(id=nid).update(title=edit_title)
    # （3）提交后重定向
    return redirect("/depart/list/")

