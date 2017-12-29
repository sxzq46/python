# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/12/26

import json,time,os
from conf import settings

def mysql_db_handler(conn_parms):
    pass

def file_storage_handler(conn_parms,account,password):
    db_dir = "%s\\%s" %(conn_parms['path'],conn_parms['accounts'])
    account_file = "%s\\%s.json" %(db_dir,account)
    if os.path.isfile(account_file):
        with open(account_file,'r') as f:
            account_data = json.loads(f)
            if account_data['password'] == password:
                return account_data
            else:
                print("Account ID or password is incorrect!")
    else:
        print("Account %s does not exist" %account)




def db_handler_api(account,password):
    conn_parms = settings.DATABASE
    if conn_parms['engine'] == 'mysql':
        return  mysql_db_handler(conn_parms,account,password)
    elif conn_parms['engine'] == 'file_storage':
        return file_storage_handler(conn_parms,account,password)