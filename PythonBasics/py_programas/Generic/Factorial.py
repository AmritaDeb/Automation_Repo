def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
        yield f
ob=fact(3)
i=iter(ob)
print(i)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))