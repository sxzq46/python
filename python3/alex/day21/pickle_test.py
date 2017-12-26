# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/12/25


import pickle

def foo():
    print('ok')


data = pickle.dumps(foo)
f = open('PICKLE_TEST','wb')
f.write(data)
f.close()