# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2018/1/15

import time

def f1(req):
    return [b'<h1>Hello, book!</h1>']

def f2(req):
    return [b'<h1>Hello, web!</h1>']


def current_time(req):
    cur_time = time.ctime(time.time())
    f = open("current_time.html","rb")
    data = f.read()
    data = str(data,"utf8").replace("!cur_time!",str(cur_time))
    return [data.encode("utf8")]