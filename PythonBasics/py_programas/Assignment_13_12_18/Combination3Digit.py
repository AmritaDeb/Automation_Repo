import itertools
class Combination3Digit:
    def combination3Digit(self):
        x = [1,5,3]
        n = 3
        aa = [list(comb) for i in range(1, n + 2) for comb in itertools.combinations(x, i)]
        print(aa)
ob=Combination3Digit()
ob.combination3Digit()