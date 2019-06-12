"""
Python Program to Find the Sum of Elements in a List Recursively
"""

def sumList(l):
    sum = 0
    if len(l)<1:
        return 0
    sum = sum + l[0]
    l.remove(l[0])
    return (sum + sumList(l))
print(sumList([10,50,30,40]))

