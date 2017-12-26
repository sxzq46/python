# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/12/25


import shelve

f = shelve.open(r'shelve_text')

# f['info'] = {'name':'shixz','age':'20'}
# f['shopping'] = {'name':'alex','price':'100'}
data = f.get('shopping')
print(data)





#
# d = {'name':'alex','price':'100'}
# print(d.get('name','male'))
