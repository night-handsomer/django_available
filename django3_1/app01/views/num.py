"""靓号管理"""
from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import NumModelForm, NumEditModelForm
from app01.utils.search import SearchingBox

# 最新版本---靓号列表
def num_list(request):

    """
    使用封装的分页功能改造代码
    """
    # 搜索的字典
    dict = SearchingBox(request, dict_name="mobile")
    # 返回搜索字典变量
    data_dict = dict.data_dict
    # 查询集
    queryset = models.PrettyNum.objects.filter(**data_dict).order_by("-level")
    # 分页功能
    new_code_object = Pagination(request, queryset)

    context = {
        "queryset": new_code_object.page_queryset,
        "search_data": dict.search_data,
        "page_string": new_code_object.html()
    }
    return render(request, "num_list.html", context)


# 较新版本---靓号列表
# def num_list(request):
#
#     """
#     使用封装的分页功能改造代码
#     """
#     # data_dict = {}
#     # search_data = request.GET.get("search", default="")
#     # if search_data:
#     #     data_dict["mobile__contains"] = search_data
#     # queryset = models.PrettyNum.objects.filter(**data_dict).order_by("-level")
#     dict = SearchingBox(request, dict_name="mobile")
#     data_dict = dict.data_dict
#     queryset = models.PrettyNum.objects.filter(**data_dict).order_by("-level")
#     new_code_object = Pagination(request, queryset)
#
#     context = {
#         "queryset": new_code_object.page_queryset,
#         "search_data": dict.search_data,
#         "page_string": new_code_object.html()
#     }
#     return render(request, "num_list.html", context)


# 老版本
    # 利用循环生成更多数据，用于学习分页
    # for i in range(300):
    #     models.PrettyNum.objects.create(mobile="18888888888", price=10, level=1, status=1)


    # （1）首先要获取数据表中存储的所有号码，注意这是返回的一个查询集
    # 补充一个知识点，如果我们想要将取得的数据进行排序显示，那么可以使用.order_by()方法
    # 如果想按照id来排序，那么有升序和降序，id则是asc（升序）；-id则是降序
    # models.PrettyNum.objects.all().order_by("id/-id")【课程是按照level的desc排】
    # queryset = models.PrettyNum.objects.all().order_by("-level")

    """这是改进用字典传数据的方法"""
    # 先创建一个空字典，目的是为了之后的判断。因为filter()的括号内为空，返回的是所有的数据，和all()等同。
    # data_dict = {}
    # 使用request.GET.get()方法来得到用户查询的信息，也就是前端的input的name值。
    # 当然了，这里指定default的目的是想要查询后还能够将查询的值作为占位符留在输入框中。【源码中default是None】
    # search_data = request.GET.get("search", default="")
    # 做一个判断，如果是空，直接是返回所有的数据。不为空，就将其赋值为刚才的空字典的。
    # 值得注意的是，dict["xx"] = yy 就是dict = {"xx": yy}
    # if search_data:
    #     # 这里的mobile__contains属性就是说，筛选字符串中包含用户所提交的字符的那些数据。
    #     data_dict["mobile__contains"] = search_data   # 这句其实就是data_dict = {"mobile__contains": value}
    # 按照用户提交的要求进行查询得到的查询集，尽管是使用字典查询，但一样可以按照自己的想法来进行排序展示。
    # queryset = models.PrettyNum.objects.filter(**data_dict).order_by("-level")

    """分页的代码, 在靓号列表num_list函数中"""
    # (1) 获取数据的条数，计算出应该分多少页。
    # ---获取数据的总条数
    # total_count = models.PrettyNum.objects.filter(**data_dict).order_by("-level").count()
    # # ---计算总的页数（即页码）,假定一页展示10行数据。
    # page_size = 10
    # # ---可以利用divmod(x, y)函数，就是x / y = (a, b)，其中a为商，b为余数，若能整除则b=0；
    # total_page, rest = divmod(total_count, page_size)
    # if rest:
    #     total_page += 1

    # (2)根据用户提交的page值，计算出要展示分页的数据，即设置选择页面的选项框
    # ---（1）获取用户提交的页面值（就是第几个页面），因为从url中获取，所以使用request.GET.get()方法
    # page = int(request.GET.get("page", default="1"))  # 【注意：该方法获取的是字符串类型，因此要进行int转换】
    #
    # # ---（2）寻找换算关系，根据page生成能够看见的页面。假设一次可以看10页, 且以起始页为page；
    # start = (page - 1) * page_size  # 如：一次看10页面，第一页是0-10，算法就是如此
    # end = page * page_size
    #
    # # (3)这是页面选项框的代码
    # # ---计算当前页面选项框的前两页和后两页
    # plus = 1   # 解决前闭后开问题
    # option_size = 2
    # start_page = page - option_size
    # end_page = page + option_size + plus  # 因为range()的范围是前闭后开区间，因此要加个plus
    #
    # # ---生成前面的页面选项框的标签
    # page_list = []

    # ---(加入限制代码！)因为我们设置的是一次展示五个选项框，所以如果只有5页，那就直接展示；
    # if total_page <= 2*option_size+1 or start_page <= 0:
    #     # ---起始直接为1
    #     start_page = 1
    #     end_page = total_page + plus
    # else:
    #     if end_page-1 >= total_page:
    #         end_page = total_page + plus
    #         start_page = total_page - 2*option_size




    # queryset = models.PrettyNum.objects.filter(**data_dict).order_by("-level")[start: end]

    # return render(request, "num_list.html",
    #               {"queryset": queryset, "search_data": search_data, "page_string": page_string})


# 新建靓号
def num_add(request):

    if request.method == "GET":
        # 实例化form然后传入前端页面
        form = NumModelForm()
        return render(request, "num_add.html", {"form": form})

    # post请求的数据校验

    form = NumModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/num/list/")
    else:
        return render(request, "num_add.html", {"form": form})


"""那么我们在编辑的视图函数num_edit()就可以使用上述针对编辑而写的NumEditModelForm类了"""
# 编辑靓号
def num_edit(request, nid):
    if request.method == "GET":
        # 获取用户点击的id，根据id取出对应的数据
        edit_data = models.PrettyNum.objects.filter(id=nid).first()
        """使用ModelForm的组件来对所要编辑的那行数据进行编辑"""
        # （1）首先将NumModelForm()实例化对象为form，
        # （2）并且将获得的那行数据对象edit_data赋给instance属性
        form = NumEditModelForm(instance=edit_data)
        # （3）然后才是将form传回到前端用于渲染
        return render(request, "num_edit.html", {"form": form})

    # POST请求，将用户编辑提交的数据保存
    # （1）还是先获取用户点击的id值
    sub_data = models.PrettyNum.objects.filter(id=nid).first()
    # （2）使用modelform的组件进行数据校验，当然了，这里需要还要实例化对象
    #     这里需要注意，必须给出data和instance的属性值，因为前者是获取数据的，从request.POST得到；
    #     后者是把数据更新到具体的那一行，否则最好会成为提交新的数据而已。注意，这时候的form和GET请求的不一样了。
    form = NumEditModelForm(data=request.POST, instance=sub_data)
    # （3）进行数据校验，如果成功就重定向回靓号列表
    if form.is_valid():
        form.save()
        return redirect("/num/list/")
    # （4）如果校验不成功，那么就返回错误信息
    else:
        return render(request, "num_edit.html", {"form": form})


# 删除靓号
def num_delete(request, nid):

    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect("/num/list/")
