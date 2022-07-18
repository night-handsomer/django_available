from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from app01.utils.bootstrap import BootStrapModelForm
######################################  ModelForm实例  ###################################

# 添加用户---modelform改进
# （1）从django的导入forms，ModelForm组件就在forms中。
from django import forms   # 这可以提上去前面的。


# （2）定义modelform的类---以下是一种固定格式
class UserModelForm(BootStrapModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'account', 'create_time', 'gender', 'depart']

class NumModelForm(BootStrapModelForm):
    """使用ModelForm来做"""
    # 想对mobile的校验进行正则表达式校验
    # validators是校验器，正则表达式r'^159[0-9]+$'就是校验的表达式。^是表达式开始的符号，$是结束符号，
    # 式子意思是159开头，10位数字。
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^159[0-9]+$', "请以159开头")]
        # validators=[RegexValidator(r'^1[3-9]\d{9}$', "1开头，第二个数组3-9中选，然后后面跟9个数字")]
    )

    class Meta:
        model = models.PrettyNum
        # 下面是自定义的字段
        # fields = ["mobile", "price", "level", "status"]
        # 事实上modelform给我们提供了一些方法可以不用我们自己自定义，
        # 例如下面的“__all__”就是内置的方法，直接取出model中数据库定义的所有字段
        fields = "__all__"
        # 当然了如果我们想要剔除某些字段也可以使用exclude = ["要排除的字段名（如level）"]，具体如下：
        # exclude = ["level"]


    """下面这个是调整渲染样式的源码法"""
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     for name, field in self.fields.items():
    #         field.widget.attrs = {"class": "form-control"}

    """数据校验：钩子方法"""
    # 定义clean_字段名()的函数来实现。
    def clean_mobile(self):
        # 获取用户输入的手机号内容
        txt_mobile = self.cleaned_data["mobile"]

        if len(txt_mobile) != 11:
            # 抛出错误异常
            raise ValidationError("格式错误")
        # 验证通过则返回txt_mobile
        return txt_mobile


"""实际上对于编辑的操作，我们也是可以再针对编辑来定义一个专有的类的"""
class NumEditModelForm(BootStrapModelForm):
    # 使用forms.CharField()的disabled属性，重新定义mobile，
    # 从而就可以使手机号不可编辑了，这种方法是可以显示手机号但不能更改的。
    mobile = forms.CharField(disabled=True, label="手机号")

    class Meta:
        model = models.PrettyNum
        # 比如编辑的话，我们想让用户不能编辑手机号码那可以有两种方法
        # （1）直接在fields里面去掉---这里用exclude方法。
        fields = ["mobile", "price", "level", "status"]
        # 使用exclude方法。但是这种方法属于直接屏蔽掉了mobile。
        # exclude = ["mobile"]
        # （2）第二种就是直接在class Meta之前重新定义mobile的model属性，看Meta之前。

    """下面这个是调整渲染样式的源码法"""
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     for name, field in self.fields.items():
    #         field.widget.attrs = {"class": "form-control"}

    """定义手机号不能重复的错误提示，钩子方法"""
    def clean_mobile(self):
        # 获取用户提交的手机号
        txt_mobile = self.cleaned_data["mobile"]
        # 从数据库中校验是否存在，这里要注意在编辑的时候要排除掉自己，因此只给mobile是不行的
        # exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
        # 解决方法就是还要给出一个id。下面语句意思是说id！=2且电话号码为txt_mobile的那一条数据是否存在
        # 也就是说通过这种方法来排除自己
        # exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exclude(id=2)  # 不严谨
        # 正确的写法
        exists = models.PrettyNum.objects.filter.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()

        if exists:
            raise ValidationError("手机号已存在")
        return txt_mobile