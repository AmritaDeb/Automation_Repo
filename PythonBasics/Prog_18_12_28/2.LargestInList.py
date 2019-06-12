# write a program to find the largest in a list

class LargestInList:
    def findLargestUsingLC(self,l):
        l2=[i for i in sorted(l)]
        print(l2[-1])
    def findLargest(self,l):
        l.sort()
        print(l[-1])

ob=LargestInList()
l = [45, 85, 65, 74]
ob.findLargestUsingLC(l)
ob.findLargest(l)