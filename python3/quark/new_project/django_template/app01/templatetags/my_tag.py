# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2018/1/22
from django import template
from django.utils.safestring import  mark_safe

register = template.Library()

# 参数不能超过2个
@register.filter
def my_add100(v1,v2):
    return v1+v2

# 不能用于if语句
@register.simple_tag
def my_add(v1,v2,v3):
    return v1+v2+v3