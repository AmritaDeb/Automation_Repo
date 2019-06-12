#   wap to remove the duplicate value from the list (try with list comrahension)
class RemoveDuplicateFromList:
    def removeDuplicate(self,l):
        l1=[]
        for i in l:
            if i not in l1:
                l1.append(i)
        print(l1)
    def removeDuplicateUsingLC(self,l):
        l1=[]
        [l1.append(i) for i in l if i not in l1]
        print(l1)

ob=RemoveDuplicateFromList()
l=[12,45,65,32,12,78,45,85]
ob.removeDuplicate(l)
ob.removeDuplicateUsingLC(l)