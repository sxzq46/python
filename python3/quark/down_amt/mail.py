#__author: XiangzhongShi
#date: 2017/8/10

import smtplib
from email.mime.text import MIMEText


mail_port = 25
mail_host = 'mail.quarkfinance.com'
mail_user = 'xiangzhongshi'
mail_pass = '123456@Q'
mail_postfix = 'quarkfinance.com'


def send_mail(itop_id, to_list, sub, content):
    me = itop_id + " 降额申请 " + "<" + mail_user + "@" + mail_postfix + ">"
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

if __name__ == '__main__':
    send_mail()