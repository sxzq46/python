# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/12/25


import json

# f = open('JSON_TEST','r')
# data = f.read()
# data = json.loads(data)
# print(data['name'])

#--------load

f = open('JSON_TEST','r')
data = json.load(f)
print(data['name'])