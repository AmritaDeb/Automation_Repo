def fib(n):
    a,b=0,1
    while n>1:
        yield a
        a,b = b,a+b

ob=fib(5)
i=iter(ob)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))