#__author: XiangzhongShi
#date: 2017/7/25

# a = ['guoying','jiashun','xiaoyu','qinpeng','qinren','shixz']

#增删改查
#查
# print(a[1:]) #取到最后
# print(a[1:-1]) #取到倒数第二值
# print(a[1::2])#从左到右，步长为2
# print(a[4::-2])
#增
# a.append('xiuxia')
# print(a)
# a.insert(1,"dongshun")
# print(a)
#改
# a[1] = 'ruixue'
# print(a)
# a[1:3]=['a','b']
# print(a)
#删 remove pop del
# a.remove('qinren')
# print(a)
# b=a.pop(1)
# print(a)
# print(b)
#
# del a[0]

#count
# a = [1,2,3,1,5]
# print(a.count(1))

#extend
# a = ['guoying','jiashun','xiaoyu','qinpeng','jiashun','qinren','shixz']
#
# first_index = a.index('jiashun')
# print first_index
# little_list = a[first_index+1:]
#
# second_index = little_list.index('jiashun')
#
# second_index_big_list = first_index + second_index +1
