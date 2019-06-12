class FindAreaOfRectangle:
    def __init__(self,length,width):
        self.l=length
        self.w=width
    def findArea(self):
        return self.l*self.w


length=int(input("Please enter the length of the rectangle: "))
width=int(input("Please enter the width of the rectangle: "))
ob=FindAreaOfRectangle(length,width)
print(ob)
print(ob.l,ob.w)
print(ob.findArea())