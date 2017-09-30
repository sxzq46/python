num1 = input("num1:")
num2 = input("num2:")
num3 = input("num3:")

if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)