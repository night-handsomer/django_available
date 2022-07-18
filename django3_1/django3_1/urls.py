"""django3_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01.views import depart, num, user, login, upload_inference, admin, pe_analysis, task, order, chart

urlpatterns = [
    # path('admin/', admin.site.urls),
    # 部门管理
    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/delete/', depart.depart_delete),
    path('depart/<int:nid>/edit/', depart.depart_edit),

    # 用户管理
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/model/form/add/', user.user_model_form_add),
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/<int:nid>/delete/', user.user_delete),

    # 靓号管理
    path('num/list/', num.num_list),
    path('num/add/', num.num_add),
    path('num/<int:nid>/edit/', num.num_edit),
    path('num/<int:nid>/delete/', num.num_delete),


    # 管理员管理
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/<int:nid>/edit/', admin.admin_edit),
    path('admin/<int:nid>/delete/', admin.admin_delete),
    path('admin/<int:nid>/reset/', admin.admin_reset),

    path('login/', login.admin_login),
    path('logout/', login.admin_logout),
    path('check/code/', login.check_words),

    # 任务管理
    path('task/list/', task.task_list),
    path('task/ajax/', task.task_ajax),
    path('task/add/', task.task_add),


    path('order/list/', order.order_list),
    path('order/add/', order.order_add),
    path('order/delete/', order.order_delete),
    path('order/edit/', order.order_edit),
    path('order/edit/save/', order.order_save),
    path('order/edit/save/', order.order_save),

    # 数据统计
    path('charts/list/', chart.charts_list),
    path('charts/bar/', chart.charts_bar),

    # 姿态估计
    path('test/', upload_inference.up_test),

    # 动作分析
    path('analyse/', pe_analysis.get_kpt)
]
