import math

class CalculateAvgNo:
    li = [8, 4, 6, 2]
    def calculateNoUsingMath(self):
        global li
        print(math.fsum(self.li)/len(self.li))
    def calculateNoUsingSum(self):
        global li
        print(sum(self.li)/len(self.li))
    def calculateNoUsingMyFunc(self):
        global li
        print(self.MyFunc(self.li)/len(self.li))
    def MyFunc(self,l):
        sum=0
        for i in range(len(l)):
            sum+=l[i]
        return sum

ob=CalculateAvgNo()
ob.calculateNoUsingMath()
ob.calculateNoUsingSum()
ob.calculateNoUsingMyFunc()
