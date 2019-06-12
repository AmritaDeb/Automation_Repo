class IntegerNotDivisible:
    def notDivisible(self):
        lower = 1;upper = 50;n1=2;n2=3
        for i in range(lower, upper + 1):
            if i % n1 != 0 and i% n2 !=0:
                print(i)
ob= IntegerNotDivisible()
ob.notDivisible()