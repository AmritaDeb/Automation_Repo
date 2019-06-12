#   wap to find the maximum elements from a list using reduce
import functools
class MaxElementInList:
    def maxElementInList(self,l):
        op=functools.reduce(lambda a,b:a if a>b else b,l)
        print(op)

ob=MaxElementInList()
l=[10,50,40,32]
ob.maxElementInList(l)