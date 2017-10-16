# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/10/13



# s = (x*2  for x in range(10))
#
# print(next(s))
# print(next(s))  #等价于s.__next__() in Py2: s.next()
# print('====')
# for i in s:
#     print(i)

#
# def fib(max):
#     n, before, after = 0, 0, 1
#     while n < max:
#         yield before
#         before,after=after,before+after
#         n = n + 1
#
# g = fib(8)

def bar():
    print('ok1')
    count = yield 1
    print(count)

    yield 2

b = bar()
b.send(None)    #等同于next(b) 第一次send前如果没有next，只能传一个send(None)
b.send('eeee')