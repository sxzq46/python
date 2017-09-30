
def str2int(n):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}[s]

    return reduce(fn, map(char2num, n))


print str2int('bafd')



