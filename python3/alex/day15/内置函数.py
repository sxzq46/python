# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/10/9

from functools import reduce

# seq = ['one', 'two', 'three']
# for i, j in enumerate(seq):
#     print(i, seq[i])


# str = ['a','b','c','d']
# def fun1(s):
#     if s != 'a':
#         return s
# ret = filter(fun1, str)
# print(ret)
# print(list(ret))

# str = ['a','b','c','d']
# def fun2(s):
#     return s + "shixz"
#
# ret = map(fun2, str)
# print(ret)
# print(list(ret))

# def add1(x, y):
#     return x + y
#
# print(reduce(add1,range(1,10)))


print(reduce(lambda x,y: x*y, range(1,6)))

















