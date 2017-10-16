# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/9/27


# def factorial1(x):
#     ret = 1
#     while x > 0:
#         ret = ret * x
#         x = x - 1
#     print(ret)
#
# def factorial2(x):
#     ret = 1
#     for i in range(1,x):
#         ret = ret * i
#     print(ret)
#
# factorial1(7)
#
# factorial2(6)


# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
#
# print(fact(5))

def fibo(n):
    if n == 0 or n == 1:
       return n
    return fibo(n-1) + fibo(n-2)
print(fibo(8))