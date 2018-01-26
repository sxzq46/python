# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2018/1/9


# try:
#     # inp = input('请输入序号：')
#     # i = int(inp)
#     li = [11, 22, 33, 44, 55]
#     li[2]
#     int('123')
# except IndexError as i:
#     print(i)
# except ValueError as v:
#     print(v)
# except Exception as e:
#     print(e)
# else:
#     print('ok')
# finally:
#     print('done')

class oldBoyError(Exception):
    def __int__(self, message):
        self.message = message

    def __str__(self):
        return self.message


try:
    raise oldBoyError('我错了...')
except oldBoyError as e:
    print(e )


#  断言，用于强制用户服从，不服从就报错，并且可捕获，但是一般不捕获
print(23)
assert 1 == 2
print(456)