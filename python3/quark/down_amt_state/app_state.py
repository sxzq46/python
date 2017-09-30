#__author: XiangzhongShi
#date: 2017/8/11
#-*- coding:utf-8 -*-


import cx_Oracle

def select_app(code):
    conn = cx_Oracle.connect('appread/appread_2016@172.30.30.60:1521/COREPRD.quark.com')
    cr1 = conn.cursor()
    sql = "select app_code,product_code,product_name,app_status,thd_deal_status,is_send_dr from app.app_queue where app_code in(%s) AND thd_deal_status = 'DR_THD_APPRING'" %(code,)
    cr1.execute(sql)
    rs1 = cr1.fetchall()
    cr1.close()
    conn.close()
    if rs1:
        print("审核系统点融三方审批状态为处理中！")
        L=[]
        for i in rs1:
            L.append(i[0])
        if len(L) > 1:
            update_sql = "update app.app_queue q set q.thd_deal_status = '',q.is_send_dr = 'N' where q.app_code in %s;" %(tuple(L),)
        else:
            update_sql = "update app.app_queue q set q.thd_deal_status = '',q.is_send_dr = 'N' where q.app_code in ('%s');" %(tuple(L))
        return print(update_sql)

if __name__ == "__main__":
    select_app()