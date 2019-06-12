#   wap to multiply all the elements inside a list using reduce
import functools
class MultiplyElementsInList:
    def multiplyElements(self,l):
        op=functools.reduce(lambda a,b:a*b,l)
        # op=functools.reduce(lambda a>2,l)
        print(op)

ob=MultiplyElementsInList()
l=[10,5,4,2]
ob.multiplyElements(l)