# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/10/9


import time

def logger(flag=''):
    def show_time(f):
        def inner(*x,**y):
            start = time.time()
            f(*x,**y)
            end = time.time()
            print(end-start)
            if flag == "True":
                print('日志记录')
        return inner
    return show_time

@logger('True')      #foo=show_time(foo)
def foo():
    print('foo....')
    time.sleep(2)


@logger()
def bar():
    print('bar....')
    time.sleep(3)

@logger()
def foo1(*a,**b):
    sum1 = 0
    for i in a:
        sum1 += i
    print(sum1)
    time.sleep(2)

foo1(1,2)
bar()
foo()