#__author: XiangzhongShi
#date: 2017/7/26


product_list = [('iphone6s',5800),
                ('MacBook',9000),
                ('coffee',32),
                ('book',80),
                ('bicyle',1500)]

saving = input('your saving:')
shopping_car = []


if saving.isdigit():
    saving = int(saving)
    while True:

        for i,v in enumerate(product_list,1):
            print(i,'>>>',v)
        choice = input('选择购买商品编号或按q退出：')


        if choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice <=len(product_list):
                p_item = product_list[choice-1]
                if p_item[1] < saving:
                    saving -=p_item[1]
                    shopping_car.append(p_item[0])
                else:
                    print('余额不足！，还剩下%s' %saving)


                print(p_item)
            else:
                print('编码不存在。')


        elif choice == 'q':
            print('您已经购买如下商品：')
            for j in shopping_car:
                print(j)
            print('您还剩%s元钱'%saving)
            break

        else:
            print('invalid input')
else:
    print('invalid input')