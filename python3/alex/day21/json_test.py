# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/12/25


import json
#
# dic = {'name':'shixz','age':'18'}
# data = json.dumps(dic)
# f = open('JSON_TEST','w')
# f.write(data)


#----------dump
dic = {'name':'shixz','age':'18'}
f = open('JSON_TEST2','w')
json.dump(dic,f)
f.close