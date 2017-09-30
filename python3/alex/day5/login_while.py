#__author: XiangzhongShi
#date: 2017/7/24


_user = "shixz"
_passwd = "abc123"

counter = 0
while counter < 3:
    username = input("Username:")
    password = input("Password:")

    if username == _user and password == _passwd:
        print("welcome %s login..." % _user)
        break
    else:
        print("Invalid username or password !")
    counter += 1

    if counter == 3:
        keep_going_choice = input("继续输入吗？(Y/N)")
        if keep_going_choice == "Y":
            counter = 0

else:
    print("登录失败！")