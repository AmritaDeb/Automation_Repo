#   Wap to print the odd no
class PrintOddNo:
    def printOddNo(self,l):
        op=filter(lambda l:l%2!=0,l)
        print(list(op))
ob=PrintOddNo()
l=[11,52,12,23,64,78,92,45,63]
ob.printOddNo(l)