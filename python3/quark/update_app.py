#__author: XiangzhongShi
#date: 2017/8/9

import cx_Oracle
import smtplib
from email.mime.text import MIMEText


code = input("请输入进件编号：")
def app_sql():
    app_conn = cx_Oracle.connect('appread/appread_2016@172.30.30.60:1521/COREPRD.quark.com')
    app_cr = app_conn.cursor()
    app_code = code
    sql1 = "update app.app_queue q set q.thd_deal_status = '',q.is_send_dr = 'N' where q.app_code in(%s);" % (app_code,) + "\r\r"
    app_content = sql1
    app_conn.close()

    return app_content

("\n"
 "发送邮件\n")

mailto_list = ['xiangzhongshi@quarkfinance.com','guoyingzhang@quarkfinance.com']
mail_port = 25
mail_host = 'mail.quarkfinance.com'
mail_user = 'xiangzhongshi'
mail_pass = '123456@Q'
mail_postfix = 'quarkfinance.com'


def send_mail(to_list, sub, content):
    me = " 降额申请 " + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content, _subtype='plain', _charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP(mail_host, mail_port)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception as e:
        print(str(e))
        return False

if __name__ == "__main__":
    send_mail(mailto_list, "降额申请-审核", app_sql())