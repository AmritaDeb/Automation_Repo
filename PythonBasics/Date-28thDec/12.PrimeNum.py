#   wap to write the prime numbers from 1 to 1000
class PrimeNo:
    def primeNo(self, lower, upper):
        for num in range(lower, upper + 1):
            if num > 1:
                for i in range(2, num):
                    if num % 2 == 0:
                        break
                else:
                    print(num)


ob = PrimeNo()
ob.primeNo(1, 1000)