"""
    搜索功能

"""
from app01 import models

class SearchingBox(object):

    def __init__(self, request, dict_name, data_dict=None):
        """

        :param request: 请求体
        :param dict_name: 你想查询的字段名(这个一定是和models里面的键是匹配的)
        :param data_dict: 查询字典，必须这么设置
        """
        # 这是一个标准写法，如果不这么写，直接传参为 data_dict = {}是不行的。
        if data_dict is None:
            data_dict = {}
        self.data_dict = data_dict
        # 获取搜索框的关键字
        search_data = request.GET.get("search", default="")
        # 设置字段
        if search_data:
            self.data_dict["{}__contains".format(dict_name)] = search_data
        # 返回一个留置值，就是查询的关键字
        self.search_data = search_data
