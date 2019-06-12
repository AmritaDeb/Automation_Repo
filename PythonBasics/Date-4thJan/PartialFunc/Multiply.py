from functools import partial

def multiply(a,b):
    return a*b

print(multiply(2,3))

mul=partial(multiply,b=9)
print(mul(6))

