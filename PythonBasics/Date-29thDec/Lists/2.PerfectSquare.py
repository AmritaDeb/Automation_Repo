#   wap to find all numbers in a range which are perfect square and sum of all digits in the number less than 100
class PerfectSquare:
    def perfectSquare(self):
        sq=[a**2 for a in range(1,10)]
        print(sq)

ob=PerfectSquare()
ob.perfectSquare()