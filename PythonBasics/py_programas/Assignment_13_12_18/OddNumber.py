class OddNumber:
    def oddumber(self):
        lower=int(input("Enter the lower range: "))
        upper=int(input("Enter the upper range: "))
        for i in range(lower,upper+1):
            if i%2==1:
                print(i)
ob=OddNumber()
ob.oddumber()