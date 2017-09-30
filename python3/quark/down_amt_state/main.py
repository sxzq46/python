#__author: XiangzhongShi
#date: 2017/8/11


import app
import quotabid
import mail

itop_id = input("请输入ITOP编号及标题：")
code = input("请输入进件号，格式为：'170707002009010004','170707002009010003' :")

mailto_list = ['xiangzhongshi@quarkfinance.com']

if app.select_app(code):
    app.select_app(code)
if quotabid.select_quotabid(code):
    quotabid.select_quotabid(code)

# mail.send_mail(itop_id, mailto_list, "降额申请-审核状态", app.select_app(into_code))
# mail.send_mail(itop_id, mailto_list, "降额申请-标的状态", quotabid.select_quotabid(into_code))