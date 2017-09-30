age = 50
#flag = True
while True:
    user_age = int(input("age:"))
    if user_age == age:
        print("yes")
        break
    elif user_age > age:
        print("bigger")
    else:
        print("smaller")
print("end")