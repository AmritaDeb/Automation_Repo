class Factorial:
    def fact(self,n):
        f=1
        for i in range(1,n+1):
            f=f*i
        return f

ob=Factorial()
print(ob.fact(5))