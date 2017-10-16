# -*- coding: utf-8 -*-
# __author: XiangzhongShi
# date: 2017/10/10




login_status = False

page = ['home','finance','book']

def login(auth):
    def business(func):
        def inner(*x, **y):
            global login_status
            if login_status == False:
                username = input('username:')
                password = input('passwd:')
                if auth == 'jingdong':
                    with open('jingdong', 'r', encoding='utf8') as f_read:
                        jingdong_auth = eval(f_read.read())
                    if username in jingdong_auth and password == jingdong_auth[username]:
                        print('登录成功！')
                        func(*x, **y)
                        login_status = True
                    else:
                        print('用户名或密码错误！')
                else:
                    with open('weixin', 'r', encoding='utf8') as f_read:
                        weixin_auth = eval(f_read.read())
                    if username in weixin_auth and password == weixin_auth[username]:
                        print('登录成功！')
                        func(*x, **y)
                        login_status = True
                    else:
                        print('用户名或密码错误！')
            else:
                func(*x, **y)
                login_status = True

        return inner
    return business

@login('')
def home():
    print('welcome to home page...')

@login(auth='jingdong')
def finance():
    print('welcome to finance page...')

@login('')
def book():
    print('welcome to book page...')


if __name__ == '__main__':
    print('欢迎访问京东！')
    while True:
        choice = input('请选择：（1.home 2.finance 3.book），或输入exit退出:')
        choice = choice.strip()
        if len(choice) == 0: continue
        elif choice == "home":
            home()
        elif choice == "finance":
            finance()
        elif choice == "book":
            book()
        elif choice == "exit":
            break
        else:
            print('无此项！')