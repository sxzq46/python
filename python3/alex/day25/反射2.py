# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2018/1/9


import s2

inp = input('请输入URL：')

if hasattr(s2, inp):
    func = getattr(s2, inp)
    result = func()
    print(result)
else:
    print('404')