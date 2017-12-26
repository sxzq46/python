# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/12/12


import hashlib

m = hashlib.md5()
print(m)
m.update('hello world'.encode('utf8'))
print(m.hexdigest())

