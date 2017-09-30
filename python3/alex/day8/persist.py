# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/9/1


import sys,time

# for i in range(30):
#     print('*',end='',flush=True)
#     time.sleep(0.1)

f_read = open('qian','r',encoding='utf8')
f_write = open('qian3','w',encoding='utf8')
num = 0
for i in f_read:
    num += 1
    if num ==2:
        i = ''.join([i.strip(),'shixz\n'])
    f_write.write(i)

f_read.close()
f_write.close()