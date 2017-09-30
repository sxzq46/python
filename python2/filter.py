import math
def prime(s):
    if s == 1:
        return True
    else:
        return [] != [s for x in range(2, int(math.sqrt(s))+1) if s % x == 0]
print filter(prime, range(1,100))