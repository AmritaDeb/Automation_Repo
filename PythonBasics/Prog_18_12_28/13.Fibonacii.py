#   wap for fibonacci series
class Fibonacii:
    def fibonacii(self, n):
        a, b = 0, 1
        for i in range(n):
            print(a)
            a, b = b, a + b
    def fibonaciiYield(self,n):
        a, b = 0, 1
        while n > 1:
            yield a
            a, b = b, a + b

ob = Fibonacii()
ob.fibonacii(4)
m=ob.fibonaciiYield(2)
i=(iter(m))
print(i)
for x in range(5):
    print(next(i))