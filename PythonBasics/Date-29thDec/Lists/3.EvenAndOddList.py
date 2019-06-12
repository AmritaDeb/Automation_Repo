# wap to put even and odd elements in a list into 2 different list
class EvenAndOddList:
    def evenAndOdd(self,l):
        even=[]
        odd=[]
        for i in l:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        print("Even element: ",even)
        print("Odd element: ",odd)
ob=EvenAndOddList()
l=[4,7,9,6,2,3,5]
ob.evenAndOdd(l)