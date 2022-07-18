"""
自定义的分页组件，以后如果想要使用这个分页组件，你需要做如下几件事情：
(1)views.py中：
    # 1.根据自己的情况去筛选自己的数据
    # 2.实例化分页对象
        1）获取到分完页的数据
        2）生成的页码
    # 3.返回页面

(2)在html文件中，使用：
        <ul class="pagination" style="float: left;">
            {{ page_string }}
        </ul>

"""
import copy
from django.utils.safestring import mark_safe


class Pagination(object):

    def __init__(self, request, queryset, page_size=10, page_params="page", option_size=3, plus=1):
        """
        :param request: 请求的对象
        :param queryset: 符合条件的数据查询集
        :param page_size: 一次展示多少个页面
        :param page_params: 在前端的name值是什么（也就是在url中获取传递的参数），这里是page
        :param option_size: 想要前后可见的范围
        :param plus: 解决前闭后开的变量
        """
        # 解决bug2，也就是使得url能够保留原有的并且拼接后续添加的。
        query_dict = copy.deepcopy(request.GET)   # 首先深复制一份原有的url信息，这是一个查询字典QueryDict
        query_dict._mutable = True                # 将查询字典的_mutable属性值置为True
        self.query_dict = query_dict              # 这样就能取得用于url拼接的值了。


        page = request.GET.get(page_params, "1")
        # 判断page是否合法，这里给出的判断是不是10进制数字
        if page.isdecimal():
            page = int(page)
        else:
            page = 1

        self.page = page
        self.page_size = page_size

        # 一次能展示的页数的起止计算
        self.start = (page - 1) * page_size
        self.end = page * page_size

        # 一次展示的queryset
        self.page_queryset = queryset[self.start: self.end]

        # 计算要分多少页码
        self.total_count = queryset.count()  # 计算总的数据条数
        self.total_page, self.rest = divmod(self.total_count, self.page_size)
        if self.rest:
            self.total_page += 1
        # 计算页码一次能展示的范围，就是给页码分页
        self.start_page = self.page - option_size
        self.end_page = self.page + option_size + plus
        # ---(加入限制代码！)因为我们设置的是一次展示五个选项框，所以如果只有5页，那就直接展示；
        if self.total_page <= 2 * option_size + 1 or self.start_page <= 0:
            # ---起始直接为1
            self.start_page = 1
            self.end_page = self.total_page + plus
        else:
            if self.end_page - 1 >= self.total_page:
                self.end_page = self.total_page + plus
                self.start_page = self.total_page - 2 * option_size
        self.page_params = page_params

    # 生成分页框的html代码
    @property
    def html(self):
        page_list = []

        self.query_dict.setlist(self.page_params, [1])
        self.query_dict.urlencode()
        # ---添加首页和上一页
        # ~~~首页
        first_page = '<li><a href="?{}">首页</a></li>'.format(self.query_dict.urlencode())
        page_list.append(first_page)
        # ~~~上一页
        if self.page > 1:
            self.query_dict.setlist(self.page_params, [self.page - 1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_params, [1])
            prev = '<li><a href="?page={}">上一页</a></li>'.format(self.query_dict.urlencode())
        page_list.append(prev)

        for i in range(self.start_page, self.end_page):
            self.query_dict.setlist(self.page_params, [i])
            # 这个是下面选项框的标签！！！别弄再弄混了
            if i == self.page:  # 如果是点击的当前的页面，那么设置一个高亮的选中标志
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:  # 否则，就是普通的选项框。
                ele = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_list.append(ele)

        # ---添加下一页
        # ~~~下一页
        if self.page < self.total_page:
            self.query_dict.setlist(self.page_params, [self.page + 1])
            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_params, [self.total_page])
            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        page_list.append(prev)
        # ~~~尾页
        self.query_dict.setlist(self.page_params, [self.total_page])
        first_page = '<li><a href="?{}">尾页</a></li>'.format(self.query_dict.urlencode())
        page_list.append(first_page)
        search_str = """
            <li>
                <form action="" method="get" style="float: left; margin-left: -1px; ">
                    <input type="text" name="page" class="form-control" placeholder="页码"
                        style="position: relative; display: inline-block; width: 80px; border-radius: 0;">
                    <button style="border-radius: 0; margin-left: -5px; margin-bottom: 2px" class="btn btn-default" type="submit">跳转</button>
                </form>
            </li>
                """
        page_list.append(search_str)

        page_string = mark_safe("".join(page_list))
        return page_string


