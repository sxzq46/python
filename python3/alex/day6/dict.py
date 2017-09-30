#__author: XiangzhongShi
#date: 2017/7/28


# dic={'name':'shixz','age':28,'hobby':{'girl_name':'guoqian','age':'27'}}

# print(dic['hobby'])
#
#
# dic2=dict([['name','shixz'],])
#
# print(dic2)

# dic5={'name':'shixz','age':28,'hobby':{'girl_name':'guoqian','age':'27'}}

# dic={5:'777',2:'999',4:'555'}
#
# print(sorted(dic.items()))

# dic5={'name':'shixz','age':18}
# for i in dic5:
#     print(i,dic5[i])


# a='abc'
# b='123'
# d='444'
# c='++'.join([a,b,d])
# print(c)


st='hello kitty {name}'

print(st.count('l'))        # 统计元素个数
print(st.capitalize())      # 首字母大写
print(st.center(50,'-'))    # 居中
print(st.endswith())        # 以某个内容结尾
print(st.startswith())      # 以某个内容开头
print(st.expandtabs(tabsize=10))
print(st.find('t'))         # 查找到第一个元素，并讲索引值返回
print(st.format(name='shixz'))  #格式化输出的另一种方式
print(st.index('qqqq'))     #
print(abc123.isalnum())      # 是否包涵字母或数字
print('1234'.isdecimal())   # 识别十进制字符
print('1213'.isdigit())          # 判断是否为整型数字
print('1231'.isnumeric())        # 等于isdigit
print('123abc'.isidentifier())     # 检验非法变量
print('Abc'.islower())      # 判断是否全为小写
print('Abc'.isupper())      # 判断是否全为大写
print(' e'.isspace())       # 判断是否为空格
print('My Title'.istitle())     # 判断每个单词首字母是否为大写
print('My Title'.lower())   # 将字符统一转换成小写
print('My Title'.upper())   # 将字符统一转换成大写
print('My Title'.swapcase())        # 讲字母反转大小写
print('My Title'.ljust(20,'#'))     # 靠左
print('My Title'.rjust(20,'#'))     # 靠右
print('\tMy tLtle\n'.strip())       # 去掉左右换行或者空格字符
print('\tMy tLtle\n'.lstrip())
print('\tMy tLtle\n'.rstrip())
print('My title title'.replace('itle','lesson',1))      # 替换字符
print('My title title'.rfind('t'))     # 从右往左找第一个t的索引
print('My title title'.split('i',1))      # 以什么为分隔符分割
print('My title title'.title())     # 将每个单词首字母改为大写


# 重要的字符串方法
print(st.count('l'))
print(st.center(50,'#'))   #  居中
print(st.startswith('he')) #  判断是否以某个内容开头
print(st.find('t'))
print(st.format(name='alex',age=37))  # 格式化输出的另一种方式   待定：?:{}
print('My tLtle'.lower())
print('My tLtle'.upper())
print('\tMy tLtle\n'.strip())
print('My title title'.replace('itle','lesson',1))
print('My title title'.split('i',1))