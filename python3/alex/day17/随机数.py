# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/10/25


import random

# print(random.random())
# print(random.randint(1,9))
# print(random.choice('shixz'))
# print(random.sample([1,2,3,4,5],2))
# print(random.randrange(1,3))

# def v_code():
#     code = ''
#     for i in range(5):
#         if random.randint(0,1) == 1:
#             add_mem = random.randrange(10)
#         else:
#             add_mem = chr(random.randrange(65,91))
#         code += str(add_mem)
#     print(code)

def v_code1():
    code = ''
    for i in range(5):
        add = random.choice([random.randrange(10),chr(random.randrange(65,91))])
        code += str(add)
    print(code)

v_code1()