#   Wap to print the even no
class PrintEvenNo:
    def printEvenNo(self,l):
        op=filter(lambda l:l%2==0,l)
        print(list(op))
ob=PrintEvenNo()
l=[11,52,12,23,64,78,92,45,63]
ob.printEvenNo(l)