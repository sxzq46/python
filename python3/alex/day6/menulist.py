#__author: XiangzhongShi
#date: 2017/8/1


province = {
    '河北省':{
        '石家庄市':['长安区','桥西区','新华区','井陉矿区','裕华区','藁城区','鹿泉区'],
        '唐山市':['路北区','路南区','古冶区','开平区','丰南区','丰润区','曹妃甸区'],
        '邯郸市':['邯山区','丛台区','复兴区','峰峰矿区','肥乡区','永年区']
     },
    '浙江省':{
        '杭州市':['上城区','下城区','江干区','拱墅区','西湖区','滨江区','余杭区','萧山区','富阳区'],
        '宁波市':['海曙区','江北区','北仑区','镇海区','鄞州区','奉化区','余姚市','慈溪市','象山县','宁海县'],
        '温州市':['鹿城区','龙湾区','瓯海区','洞头区','瑞安市','乐清市','永嘉县','平阳县','苍南县','文成县','泰顺县']
    },
    '河南省':{
        '新乡市':['红旗区','卫滨区','牧野区','凤泉区','卫辉市','辉县市','新乡县','长垣县','获嘉县','原阳县','延津县','封丘县'],
        '郑州市':['中原区','二七区','金水区','惠济区','管城区','上街区','巩义市','新郑市','登封市','荥阳市','新密市','中牟县'],
        '开封市':['龙亭区','鼓楼区','禹王台区','顺河区','祥符区','兰考县','通许县','杞县','尉氏县']
    }
}

# print(province['河北省']['石家庄市'])

province_list = list(province.keys())

while True:
    print('省'.center(50,'*'))
    for i,j in enumerate(province_list,1):
        print(i,j)
    province_num = input("请出入省编号，按q(quit)退出:")
    if province_num.isdigit():
        province_num = int(province_num)
        if province_num > 0 and province_num <= len(province_list):
            city_list = list(province[province_list[province_num-1]])
            while True:
                print('市'.center(50, '*'))
                for n,m in enumerate(city_list,1):
                    print(n,m)
                city_num = input('请输入市编号，按b(back)返回上级菜单或按q(quit)退出：')
                if city_num.isdigit():
                    city_num = int(city_num)
                    if city_num > 0 and city_num <= len(city_list):
                        county_list = province[province_list[province_num-1]][city_list[city_num-1]]
                        while True:
                            for a,b in enumerate(county_list,1):
                                print(a,b)
                            quit_menu = input('按b(back)返回上级菜单或按q(quit)退出：')
                            if quit_menu == 'b':
                                break
                            elif quit_menu == 'q':
                                exit()
                            else:
                                print('错误输入！')

                    else:
                        print('编号%s不存在，请重新输入！'%city_num)
                elif city_num == 'b':
                    break
                elif city_num == 'q':
                    exit()
                else:
                    print('错误输入！')

        else:
            print('编号%s不存在，请重新输入！'%province_num)

    elif province_num == 'q':
        exit()
    else:
        print('错误输入！')