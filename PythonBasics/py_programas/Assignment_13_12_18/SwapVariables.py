class Swapping:
    def swapping(self):
        a, b = 10, 20
        print("Before swapping:", a, b)
        a,b=b,a
        print("After swapping:",a,b)
    def swappingWithTemp(self):
        a,b=40,60
        print("Before swapping:", a, b)
        temp=b
        b=a
        a=temp
        print("After swapping:", a, b)
    def swappingWithoutTemp(self):
        a,b=50,100
        print("Before swapping:", a, b)
        b=a+b
        a=b-a
        b=b-a
        print("After swapping:", a, b)
ob=Swapping()
ob.swapping()
ob.swappingWithTemp()
ob.swappingWithoutTemp()

