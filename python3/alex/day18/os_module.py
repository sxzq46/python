# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/10/25


import os

print(os.getcwd())
os.chdir(r'e:\python脚本')
print(os.getcwd())
print(os.pardir)
print(os.listdir(r'E:\python脚本\python3\alex'))
print(os.stat(r'E:\python脚本\python3\alex\day18'))
print(os.environ)