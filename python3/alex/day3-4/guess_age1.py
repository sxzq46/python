age = 50
flag = True
while flag:
    user_age = int(input("age:"))
    if user_age == age:
        print("yes")
        flag = False
    elif user_age > age:
        print("bigger")
    else:
        print("smaller")
print("end")