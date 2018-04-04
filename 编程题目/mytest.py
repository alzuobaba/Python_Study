# fib =lambda n: n if n<=2 else fib(n-1)+fib(n-2)
def fib(n):
    a, b = 0, 1
    for i in range(n):
        print('$$$$$$$$$$',i)
        a, b = b, a + b
    return b
#####################
def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
            print(cache)
        return cache[args]
    return wrap
@memo
def fib2(i):
    if i < 2:
        return 1
    return fib2(i-1) + fib2(i-2)

# #######################
# fib3 = lambda n: n if n < 2 else 2 * fib3(n - 1)
# print(fib3(2))
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(3,[3,2,1])
f(3)