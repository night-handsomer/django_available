from django import forms
from app01 import models




class BootStrap:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # 如果原来field.widget.attrs里面有属性值了，那就添加
            # 如果没有，那就直接设置else中的属性。
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label
                }


class BootStrapModelForm(BootStrap, forms.ModelForm):
    # 常规法解决form表单的样式问题---这里只展示前两个
    #
    # widgets = {
    #     "name": forms.TextInput(attrs={"class": "form-control"}),
    #     "password": forms.PasswordInput(attrs={"class": "form-control"}),
    #     "age": forms.TextInput(attrs={"class": "form-control"}),
    # }

    # 源码法

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     for name, field in self.fields.items():
    #         # 如果原来field.widget.attrs里面有属性值了，那就添加
    #         # 如果没有，那就直接设置else中的属性。
    #         if field.widget.attrs:
    #             field.widget.attrs["class"] = "form-control"
    #             field.widget.attrs["placeholder"] = field.label
    #         else:
    #             field.widget.attrs = {
    #                 "class": "form-control",
    #                 "placeholder": field.label
    #             }
    pass

class BootStrapForm(BootStrap, forms.Form):
    pass








