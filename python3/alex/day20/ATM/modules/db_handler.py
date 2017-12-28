# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/12/26

import json,time,os
from conf import settings

def mysql_handler(conn_parms):
    pass

def file_storage_handler(conn_parms):
    db_dir =



def db_handler(conn_parms):
    conn_parms = settings.DATABASE
    if conn_parms['engine'] == 'mysql':
        return  mysql_handler(conn_parms)
    elif conn_parms['engine'] == 'file_storage':
        return file_storage_handler(conn_parms)