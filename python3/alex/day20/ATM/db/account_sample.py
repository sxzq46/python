# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/12/26

import os
import json




acc_dic = {
    'id': 1234,
    'password': 'abc',
    'credit': 15000,
    'balance': 15000,
    'enroll_date': '2017-01-02',
    'expire_date': '2018-01-02',
    'pay_day': 22,
    'status': 0
}
current_dir = os.path.dirname(os.path.abspath(__file__))
accounts = "%s\\accounts\\%s.json" %(current_dir,acc_dic['id'])
print(accounts)
f = open(accounts,'w')
json.dump(acc_dic,f)
f.close()