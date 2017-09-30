#__author: XiangzhongShi
#date: 2017/7/20

_user = "shixz"
_passwd = "abc123"
#passed_authentication = False


for i in range(3):
    username = input("Username:")
    password = input("Password:")

    if username == _user and password == _passwd:
        print("welcome %s login..." % _user)
        #passed_authentication = True
        break
    else:
        print("Invalid username or password !")

else:
    print("登录失败！")