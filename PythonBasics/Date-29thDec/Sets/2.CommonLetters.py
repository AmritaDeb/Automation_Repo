#   wap to check common letters in 2 input string
class CommonLetters:
    def checkCommonLetters(self,s1,s2):
        commset = set(set(s1) & set(s2))
        if len(commset) > 0:
            print("Common letters present in two input strings")
        print(commset)
ob=CommonLetters()
s1 = input("Enter the first string:")
s2 = input("Enter the Second string:")
ob.checkCommonLetters(s1,s2)