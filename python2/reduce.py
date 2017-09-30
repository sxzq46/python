L = ['adam', 'LISA', 'barT']
def cap(s):
    return s[0].upper()+s[1:].lower()

print map(cap, L)

def prod(x, y):
    return x * y
print reduce (prod, range(1,5))

