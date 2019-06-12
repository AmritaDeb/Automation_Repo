# wap to find the largest no in a list
class LargestNoInList:
    def findLargest(self,l):
        l.sort()
        print("The largest No: ",l[-1])
        for i in reversed(l):
            print(i)
ob=LargestNoInList()
l=[45,65,78,52,98]
ob.findLargest(l)