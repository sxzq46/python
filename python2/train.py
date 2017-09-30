import time

def performance(f):
    def fn(*arg, **kw):
        print time.strftime('%Y-%m-%d',time.localtime(time.time()))
        return f(*arg, **kw)
    return fn


@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)