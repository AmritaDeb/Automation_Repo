from itertools import permutations
class Permutation3Digit:
    def permutation3Digit(self):
        n=int(input("Enter the no of elements: "))
        l1=[]
        for i in range(n):
            l2=int(input("Enter the element"))
            l1.append(l2)
        x = permutations(l1)
        for i in list(x):
            print(i)
ob=Permutation3Digit()
ob.permutation3Digit()