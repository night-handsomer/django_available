# -*- coding=utf-8 -*- 
# github: night_walkiner
# csdn: 潘迪仔

# 中间件需要导入的模块
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect

class MiddleAuth(MiddlewareMixin):
    """ 中间件 """

    def process_request(self, request):
        # request.path_info 获取用户当前请求的 url
        if request.path_info in ['/login/', '/check/code/']:

            return

        # 1. 读取当前访问用户的 session 信息，如果能读到的话就继续，否则就到登录页面
        info = request.session.get('info')
        # print(info)
        if info:
            # 这就是 return None
            return
        return redirect('/login/')


    def process_response(self, request, response):
        # print("M1.溜溜")
        return response

# class Middle2(MiddlewareMixin):
#     """ 中间件 """
#
#     def process_request(self, request):
#         print("M2.进来了")
#
#
#     def process_response(self, request, response):
#         print("M2.溜溜")
#         return response