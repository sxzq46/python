# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/10/16


# l = [1,2,3,4,5]
# d = iter(l)
# print(d)
#
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))


a = max(len(x.strip()) for x in open('abc','r'))

print(a)