"""
Python Program to Find the Fibonacci Series Using Recursion
"""

def fib(a,b,n):
    print(a)
    if n<1:
        return
    return fib(b,a+b,n-1)
fib(0,1,8)
