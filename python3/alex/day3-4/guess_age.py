
age = 88

guess_age = int(input(">>:"))

if guess_age == age:
    print("yes")
elif guess_age > age:
    print("should try smaller")
else:
    print("should try biger")
