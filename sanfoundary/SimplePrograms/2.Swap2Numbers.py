def swap1(a,b):
    print("Before swapping: a =", a, "b =", b)
    a=a+b
    b=a-b
    a=a-b
    print("After swapping: a =",a,"b =",b)

def swap2(a,b):
    print("Before swapping: a =", a, "b =", b)
    temp=a
    a=b
    b=temp
    print("After swapping: a =", a, "b =", b)
def swap3(a,b):
    print("Before swapping: a =", a, "b =", b)
    a,b=b,a
    print("After swapping: a =", a, "b =", b)


swap1(5,10)
swap2(2,8)
swap3(20,30)