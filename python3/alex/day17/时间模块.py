# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/10/13


import time,datetime

time.time() # 时间戳
time.clock() # 计算CPU执行时间
time.gmtime() # 结构化格林威治时间
time.localtime() # 结构化本地时间
local_time = time.localtime()
print(time.strftime('%Y-%m-%d %H:%M:%S',local_time)) #字符串时间
print(time.strptime('2017--10--19 16:41:38','%Y--%m--%d %H:%M:%S'))
a = time.strptime('2017--10--19 16:41:38','%Y--%m--%d %H:%M:%S')
print(a.tm_wday)
print(time.ctime())
print(time.localtime())
print(time.mktime(time.localtime()))
print(datetime.datetime.now())
print(time.time())