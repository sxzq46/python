# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/12/13


import re

# ret = re.findall('w\w{2}l','hello world')
# print(ret)
#
# ret1 = re.findall('shixz','sdccweshixzvvviwzx')
# print(ret1)

# ret = re.findall('a{1,}b','asdawbadeeeebaaab')
# ret = re.findall('a[c,d]x','acdx')

ret = re.search('(?P<id>\d{3})/(?P<name>\w{3})','www2a23rrr123/wwds')

print(ret.group())
print(ret.group('id'))
print(ret.group('name'))