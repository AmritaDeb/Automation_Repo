#   wap to genrate random numbers

import random
class GenerateRandomNumbers:
    def randomNo(self,lower,upper):
        for i in range(5):
            print(random.randint(lower,upper))

ob=GenerateRandomNumbers()
lower=int(input("Enter the lower range: "))
upper=int(input("Enter the upper range: "))
ob.randomNo(lower,upper)