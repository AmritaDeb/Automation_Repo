class FindLargestNo:
    def findLargestNo(self,list):
        list.sort()
        print(list[-1])

ob = FindLargestNo()
list = [4,8,7,9,6]
ob.findLargestNo(list)

