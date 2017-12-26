# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/12/25


import pickle

f = open('PICKLE_TEST','rb')
data = f.read()
data = pickle.loads(data)
data()