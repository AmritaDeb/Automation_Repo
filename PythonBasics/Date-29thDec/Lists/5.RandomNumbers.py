# wap to generate random numbers from 1-20, append them to the list.
import random

class RandomNumbersinList:
    def randomNo(self,n):
        l=[]
        for i in range(n):
            l.append(random.randint(1,20))
        print(l)
ob=RandomNumbersinList()
n=int(input("Enter the range: "))
ob.randomNo(n)
