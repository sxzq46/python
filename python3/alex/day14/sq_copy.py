# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/9/5


# s = [[1,2],'shixz','abc']
# s1 = s.copy()
#
#
# print(s)
# s1[1] = 3
# print(s1)
# print(s)

a = set([1,2,3,4,5])
b = set([4,5,6,7,8])
print(a.intersection(b))   #交集
print(a.union(b))   #并集
print(a.difference(b))   #差集
print(a.symmetric_difference(b))   #对称差集
a.issuperset(b)
a.issubset(b)