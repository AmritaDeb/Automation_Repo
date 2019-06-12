class Fibonacii_Yield:
    def fibonacii(self,n):
        a, b = 0, 1
        while n > 1:
            yield a
            a, b = b, a + b
ob=Fibonacii_Yield()
m=ob.fibonacii(2)
i=(iter(m))
print(i)
for x in range(6):
    print(next(i))
    raise StopIteration
