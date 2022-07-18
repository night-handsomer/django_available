from django.db import models

# Create your models here.

class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name="标题", max_length=32)

    def __str__(self):
        return self.title




class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name="员工列表", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=32)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    # create_time = models.DateTimeField(verbose_name="入职时间")
    # 如果想要所生成的时间只包含年月日（不含时分秒，可以使用DateField()）
    create_time = models.DateField(verbose_name="入职时间")
    # 所属部门---这里是有约束的，也就是已存在部门，可以理解是部门表
    depart = models.ForeignKey(verbose_name="部门", to="Department", to_field="id", on_delete=models.CASCADE)
    # django中给的约束。
    gender_chioce = (
        (1, "男"),
        (2, "女")
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_chioce)


class PrettyNum(models.Model):
    """靓号管理"""
    mobile = models.CharField(verbose_name="手机号", max_length=32)
    # 其实这里使用小数的来做是最好的。但是课程中给的是整数，那么我们按课程来吧
    # price = models.DecimalField(verbose_name="价格", max_digits=10, decimal_places=2, default=0)
    price = models.IntegerField(verbose_name="价格", default=0)
    level_chioces = (
        (1, "1级"),
        (2, "2级"),
        (3, "3级"),
        (4, "4级"),
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_chioces, default=1)
    status_chioces = (
        (1, "未占用"),
        (2, "已占用"),
    )
    status = models.SmallIntegerField(verbose_name="占用状态", choices=status_chioces, default=2)


class Admin(models.Model):
    """管理员"""
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=32)

    def __str__(self):
        # 返回对象的用户名
        return self.username

# 任务表的创建
class Task(models.Model):
    """任务表"""

    level_choices = (
        (1, "紧急"),
        (2, "重要"),
        (3, "临时")
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)
    title = models.CharField(verbose_name="标题", max_length=64)
    detail = models.TextField(verbose_name="详细信息")
    user = models.ForeignKey(verbose_name="负责人", to="Admin", on_delete=models.CASCADE)


# 订单---Ajax 的实例
class Order(models.Model):

    oid = models.CharField(verbose_name="订单号", max_length=64, null=True)
    title = models.CharField(verbose_name="商品名称", max_length=32)
    price = models.IntegerField(verbose_name="价格")
    status_choices = (
        (1, "未支付"),
        (2, "已支付")
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=1)
    # 购买用户我们暂时指向管理员表
    admin = models.ForeignKey(verbose_name="用户ID", to="Admin", on_delete=models.CASCADE)







