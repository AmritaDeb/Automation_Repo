#   wap to read a list of words and return the length of the longest 1
class ReturnLenOfLongest:
    def returnLen(self,l):
        max=len(l[0])
        temp=l[0]
        for i in l:
            if len(i)>max:
                max=len(i)
                temp=i
        return temp

ob=ReturnLenOfLongest()
l=[]
for i in range(4):
    l.append(input("Enter the elements: "))
print("The Longest length: ",ob.returnLen(l))
