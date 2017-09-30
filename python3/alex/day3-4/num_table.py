height = int(input("H:"))
width = int(input("W:"))
num_h = 1
while num_h <=height:
    num_w = 1
    while num_w <= width:
        print("#",end="")
        num_w += 1
    print()
    num_h += 1