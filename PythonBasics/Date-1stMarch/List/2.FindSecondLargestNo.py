class FindSecondLargestNo:
    def secondLargestNo(self,list):
        list.sort()
        print(list[-2])

ob = FindSecondLargestNo()
list=[]
for i in range(5):
    list.append(int(input("Enter no of elements:")))
ob.secondLargestNo(list)