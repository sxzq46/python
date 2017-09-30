# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/8/28


zone = {
    '山东' : {
        '青岛' : ['四方','黄岛','崂山','李沧','城阳'],
        '济南' : ['历城','槐荫','高新','长青','章丘'],
        '烟台' : ['龙口','莱山','牟平','蓬莱','招远']
    },
    '江苏' : {
        '苏州' : ['沧浪','相城','平江','吴中','昆山'],
        '南京' : ['白下','秦淮','浦口','栖霞','江宁'],
        '无锡' : ['崇安','南长','北塘','锡山','江阴']
    },
    '浙江' : {
        '杭州' : ['西湖','江干','下城','上城','滨江'],
        '宁波' : ['海曙','江东','江北','镇海','余姚'],
        '温州' : ['鹿城','龙湾','乐清','瑞安','永嘉']
    },
    '安徽' : {
        '合肥' : ['蜀山','庐阳','包河','经开','新站'],
        '芜湖' : ['镜湖','鸠江','无为','三山','南陵'],
        '蚌埠' : ['蚌山','龙子湖','淮上','怀远','固镇']
    },
    '广东' : {
        '深圳' : ['罗湖','福田','南山','宝安','布吉'],
        '广州' : ['天河','珠海','越秀','白云','黄埔'],
        '东莞' : ['莞城','长安','虎门','万江','大朗']
    }
}

current_layer  = zone
parent_layers = []
while True:
    for key in current_layer:
        print(key)
    choice = input(">>>:").strip()
    if len(choice) == 0:continue
    elif choice in current_layer:
        parent_layers.append(current_layer)
        current_layer = current_layer[choice]
    elif choice == "b":
        if parent_layers:
            current_layer = parent_layers.pop()
    elif choice == "q":
        break
    else:
        print("无此项")