#   wap to print a length of a string
class LenOfStringInList:
    def lenOfString(self):
        l1=['hi','hello','bye']
        l2=[]
        for i in range(len(l1)):
            l2.append(len(l1[i]))
        print(l2)
        d={x:y for x,y in zip(l1,l2)}
        print(d.items())


ob=LenOfStringInList()
ob.lenOfString()