#   wap to merge to list with sorted list as an op
class Merge2List:
    def mergeLists(self):
        l1=[1,2,3]
        l2=[5,2,1]
        l=[x for i in zip(l1,l2) for x in i]
        l.sort()
        print(l)

ob=Merge2List()
ob.mergeLists()
