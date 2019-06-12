#   wap to swap the 1st and last value of list
class Swap1stWithLast:
    def swapping(self):
        l=[4,8,6,7]
        print(l)
        l[0],l[-1]=l[-1],l[0]
        print(l)
ob=Swap1stWithLast()
ob.swapping()