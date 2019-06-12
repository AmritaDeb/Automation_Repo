def fib(n):
    """ 0 1 1 2 3 5 8 """
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b

for item in fib(7):
    print(item)
