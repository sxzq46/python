# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/8/28


import cx_Oracle
code = input()

def select_WHB():
    conn = cx_Oracle.connect('quotabid/quotabid_may5@172.30.32.159:1521/biddb')
    quotbid_cr = conn.cursor()
    sql1 = "Select bid_app_code,bid_state from quotabid.qb_bid_info a where a.bid_app_code in(%s) AND  a.bid_state in('BS_XY_WSC','BS_XY_YSC','BS_XY_YQR')" %(code,)
    quotbid_cr.execute(sql1)
    WHB_state = quotbid_cr.fetchall()
    print(WHB_state)
    quotbid_cr.close()
    conn.close()
    if WHB_state:
        print("请驳回协议，并取消挂标。")
        L = []
        for i in WHB_state:
             L.append(i[0])
        print(L)
        quotabid_content = "驳回协议，请将以下进件号为 %s 取消挂标。" %(L,)
        return quotabid_content
if __name__ == "__main__":
    select_WHB()