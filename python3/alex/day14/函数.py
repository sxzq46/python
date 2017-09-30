# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/9/7

import time

# def logger(n):
#     time_format = '%Y-%m-%d %X'
#     time_current = time.strftime(time_format)
#     with open('日志','a') as f:
#         f.write('%s end action%s\n'%(time_current,n))
#
# def action1(n):
#     print('starting action1...')
#     logger(n)
#
# def action2(n):
#     print('starting action2...')
#     logger(n)
#
# def action3(n):
#     print('starting action3...')
#     logger(n)
#
# action1(33)
# action2(11)
# action3(22)

# def print_info(name,age):
#     print('name: %s' %name)
#     print('age: %d' %age)
#
# print_info(age=28,name='shixz')

# def print_info(name,age,sex='male'):
#     print('name: %s' %name)
#     print('age: %d' %age)
#     print('sex: %s' %sex)
# print_info(age=28,name='shixz',sex='female')


# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
#
# add(1,2,3,4,5)

def print_info(sex='male',*args,**kwargs):
    print(args)
    print(sex)
    print(kwargs)


# print_info(28,'shixz',sex='female')
print_info('female',28,'shixz',job='it')