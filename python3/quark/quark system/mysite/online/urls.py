# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/10/27

from django.conf.urls import url
from online import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$',views.login,name = 'login'),
    url(r'^regist/$',views.regist,name = 'regist'),
    url(r'^index/$',views.index,name = 'index'),
    url(r'^logout/$',views.logout,name = 'logout'),
]