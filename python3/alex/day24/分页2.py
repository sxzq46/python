# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2018/1/4


class foo:

    def f1(self):
        return  123

    per = property(fget=f1)

####等同于
    # @property
    # def per(self):
    #     return 123

obj = foo()
ret = obj.per
print(ret)