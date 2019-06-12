#   wap to convert the lower case string into uppercase

class StringLowerToUpper:
    def convert(self,s):
        l2u=[i.upper() for i in s]
        op=""
        for x in l2u:
            op+=x
        print(op)

ob=StringLowerToUpper()
s=input("Enter the string: ")
ob.convert(s)