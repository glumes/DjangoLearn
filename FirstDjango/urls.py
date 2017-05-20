"""FirstDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from FirstApp import views as FirstAppViews
from calc import views as calcViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 自己的视图 View,FirstDjango的视图
    url(r'^index/', FirstAppViews.index),

    # url(r'^add',calcViews.add),
    # calc 的视图
    url(r'^add/$', calcViews.add, name='add'),

    # 根据正则表达式来匹配视图
    url(r'^add/(\d+)/(\d+)/$', calcViews.add2, name='add2'),

    # 根据模板来配置文件
    url(r'^home/', FirstAppViews.home, name='home')
]
