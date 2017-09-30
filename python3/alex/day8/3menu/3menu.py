# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/9/1

with open('city','r',encoding='utf8') as f_read:
    zone = eval(f_read.read())

current_layer  = zone
parent_layers = []

while True:
    print('欢迎使用'.center(50,'*'))
    for key in current_layer:
        print(key)
    choice = input("请输入要查询的(省\市\县)或新增[a]、修改[r]、删除[d]、返回[b]，退出[q]：").strip()
    if len(choice) == 0:continue
    elif choice in current_layer:
        parent_layers.append(current_layer)
        if type(current_layer) == list:
            print("最后一级菜单。")
            current_layer = parent_layers.pop()
        else:
            current_layer = current_layer[choice]
    elif choice == "a":
        member_add = input("请输入你需要添加的省市县：").strip()
        if member_add in current_layer:
            print("此项已存在。请重新输入！")
        else:
            if type(current_layer) == list:
                current_layer.append(member_add)
            else:
                current_layer[member_add] = {}
            continue
    elif choice == "r":
        member_rev = input("请输入你需要修改的省市县：").strip()
        if member_rev in current_layer:
            member_rev_new = input("修改为：").strip()
            if type(current_layer) == list:
                current_layer[current_layer.index(member_rev)] = member_rev_new
            else:
                current_layer[member_rev_new] = current_layer[member_rev]
                del current_layer[member_rev]
            continue
        else:
            print("查无此项，请重新输入！")
    elif choice == "d":
        member_del = input("请你输入需要删除的省市县：").strip()
        if member_del in current_layer:
            parent_layers.append(current_layer)
            if type(current_layer) == list:
                del current_layer[current_layer.index(member_del)]
            else:
                del current_layer[member_del]
            continue
        else:
            print("查无此项，请重新输入！")

    elif choice == "b":
        if parent_layers:
            current_layer = parent_layers.pop()
        # else:
        #     print(current_layer)
        #     print("目前为最上级菜单，输入b后为退出系统！")
        #     break
    elif choice == "q":
        current_layer = parent_layers[0]
        print(current_layer)
        break
    else:
        print("无此项")

with open('city','w',encoding='utf8')as f_write:
    f_write.write(str(current_layer))