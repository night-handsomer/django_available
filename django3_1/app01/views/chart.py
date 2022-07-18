# -*- coding=utf-8 -*- 
# github: night_walkiner
# csdn: 潘迪仔

from django.http import JsonResponse
from django.shortcuts import render


def charts_list(request):
    return render(request, 'charts_list.html')


def charts_bar(request):
    ret = {
        "status": True,

        "color": ["#CC0033", "#3398DB"],
        "title": {
            "text": 'ECharts',
            "subtext": "子标题",
            "left": "20%",
            "textStyle": {
                "s": 30
            }
        },
        "legend": {
            "data": ['销量', "啥也不是"],
            "bottom": "0%"
        },
        "xAxis": {
            "data": ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
        },
        "series": [
            {
                "name": '销量',
                "type": 'bar',
                "data": [5, 20, 36, 10, 10, 20]
            },
            {
                "name": '啥也不是',
                "type": 'bar',
                "data": [5, 20, 36, 10, 10, 20]
            }
        ]
    }

    return JsonResponse(ret)
