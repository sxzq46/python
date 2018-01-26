# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2018/1/4


class foo:
    __v = '123'
    def __init__(self,name,age):
        self.name = name
        self.__age = age        #私有，外部无法直接访问
    @property
    def show(self):
        return self.__age


    @staticmethod
    def stat():
        return foo.__v

    def __f1(self):
        return 123

    def f2(self):
        r = self.__f1()
        return r


class bar(foo):
    def __init__(self,name):
        self.name = 123
        self.__age = 18
        super(bar, self).__init__()

    def show(self):
        print(self.name)
        print(self.__age)
        print(self.__f1)


obj = bar('shixz')
print(obj.name)
obj.show()


