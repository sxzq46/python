# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/9/11


count = 10
def outer():
    # global count
    # print(count)
    # count = 8

    count = 5
    print(count)

outer()
print(count)