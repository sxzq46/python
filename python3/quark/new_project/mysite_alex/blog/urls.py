# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2018/1/19


from django.conf.urls import url,include
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'new/story', views.introduce),
    url(r'pay/index', views.index,name="alex"),
]