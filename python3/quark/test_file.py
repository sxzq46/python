#__author: XiangzhongShi
#date: 2017/8/15


import os,time,datetime


# print(time.localtime(1505876172110))

# print(time.time())
#
# 1505901751.0412393
# 1505876172110
# a = "2017.09.08"
# b = datetime.date.today()
#
# time_array = time.strptime(a,"%Y.%m.%d")
# time_index = time.mktime(time_array)
#
# # time_current = time.mktime(b,"%Y-%m-%d")
# print(b)
# # print(time_current)
# print(time_array)
es_create_time = 1505520002884 // 1000
current_time = time.mktime(time.strptime(str(datetime.date.today()),'%Y-%m-%d'))
diff_time = (current_time - es_create_time) // ( 3600 * 24)
print(time.time())
print(current_time)
print(es_create_time)
print(diff_time)
