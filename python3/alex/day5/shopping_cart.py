#__author: XiangzhongShi
#date: 2017/7/26

product_list = [('iphone6s',5800),
                ('MacBook',9000),
                ('coffee',32),
                ('book',80),
                ('bicyle',1500)]


for i in product_list:

    print(product_list.index(i),i[0],i[1])


salary = int(input("请输入你的工资:"))
shopping_car = []
if salary.isdigit():
    while salary > 0:
        num = input("请输出你想要买的商品编号或输入quit退出:")
        product_price = int(product_list[num][1])
        salary =  salary - product_price
        if salary > 0:
            print("已加入%s到你的购物车中" % (product_list[num][0]))
            print("您的余额为:%s" % (salary))
        else:
            print("您的余额为:%s" % (salary))
            input("余额不足，请选择其他商品或退出:",)
