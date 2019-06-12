class NumbersDivisible:
    def numberDivisible(self):
        lower=int(input("Enter the lower range: "))
        upper=int(input("Enter the upper range: "))
        n=int(input("Enter the number to be divided by: "))
        for i in range(lower,upper+1):
            if i%n==0:
                print(i)
ob=NumbersDivisible()
ob.numberDivisible()