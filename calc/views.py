from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) + int(b)
    return HttpResponse(str(c))


# 根据正则表达式来匹配数据，计算结果
def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
