# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2018/1/2

'''
class Bar:
    def foo(self,arg):
        print(self,arg)

z1 = Bar()
print(z1)
z1.foo(1111)
'''


# class Bar:
#     def __init__(self,name,age):
#         self.n = name
#         self.a = age
#
#     def foo(self):
#         print(self.n)
#
# z = Bar('shixz',1)
# print(z.n)
# z.foo()


# class person:
#     def __init__(self,name,age):
#         '''
#         构造方法.构造方法的特性，类名()自动执行构造方法
#         :param name:
#         :param age:
#         '''
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print('%s:%s' %(self.name,self.age))
#
# shixz = person('施翔钟',18)
# shixz.show()

# class F:
#     def f1(self):
#         print('F.f1')
#
#     def f2(self):
#         print(F.f2)
#
# class S(F):
#     def s1(self):
#         print('S.s1')
#
#     def f2(self):
#         print('s.f2')
#         super(S, self).f2()
#
# obj = S()
#
# obj.s1()
# obj.f1()


class  F1:
    def a(self):
        print('F1.a')

class F2:
    def a(self):
        print('f2.a')

    @staticmethod
    def b():
        print('123')

    @classmethod
    def c(cls):
        print(cls)
        print('classmd')

    @property
    def per(self):
        print('321')

    @per.setter
    def per(self,val):
        print(val)



class s(F2,F1):
    pass

obj = s()
obj.a()
F2.b()
F2.c()
F2.per

F2.per = 123