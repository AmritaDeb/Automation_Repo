#   wap to add the numbers inside a list
class AddNoInList:
    def addNo(self,l):
        op=map(lambda i:i+i,l)
        print(list(op))

ob=AddNoInList()
l=[10,50,40,30]
ob.addNo(l)
