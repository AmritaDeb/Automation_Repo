class Test:
    def printing(self,a):
        print(a)
name=input("Enter your name:")
age=input("Enter your age:")
company=input("Enter your comapny name:")
ob=Test()
ob.printing(name),ob.printing(age),ob.printing(company)
"""Output:
Enter your name:Amrita
Enter your age:24
Enter your comapny name:TY
Amrita
24
TY
"""