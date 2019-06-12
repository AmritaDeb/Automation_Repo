def fact(n):
    """ 5! """
    f = 1
    for i in range(1,n+1):
        f = f*i
        yield f
for item in fact(5):
    print(item)
