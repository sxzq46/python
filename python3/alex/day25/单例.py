# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2018/1/10


# 伪单例模式例子
# class foo:
#     def __int__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(self.name,self.age)
#
# v = None
#
# while True:
#     if v:
#         v.show()
#     else:
#         v = foo('shixz',19)
#         v.show()

class foo:
    __v = None
    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = foo()
            return cls.__v

obj1 =foo.get_instance()
print(obj1)
obj2 =foo.get_instance()
print(obj2)
obj3 =foo.get_instance()
print(obj3)
