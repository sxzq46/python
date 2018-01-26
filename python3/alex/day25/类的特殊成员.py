# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2018/1/4


# class Foo:
#     def __init__(self):
#         print('init')
#
#     def __call__(self, *args, **kwargs):
#         print('call')
#
# obj = Foo()

# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __getitem__(self, item):
#         if type(item) == slice:
#             print('切片')
#         else:
#             print('索引')
#
#     def __setitem__(self, key, value):
#         print(key,value)
#     def __delitem__(self, key):
#         print(key)
#
# li = Foo('shixz', 18)
#
# r = li[8]
# print(r)


# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __iter__(self):
#         pass
#
#
# li = Foo('shixz',18)


class Mytype(type):
    def __init__(self,*args,**kwargs):
        print(123)

class Foo(object,metaclass=Mytype):
    def __init__(self):
        pass

    def func(self):
        print('hi')