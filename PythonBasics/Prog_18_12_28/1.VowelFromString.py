# write a program to print the vowels from a given string

class VowelFromString:
    def printVowelUsingLC(self):
        ip="hello india"
        vowels="aeiou"
        v=[i for i in ip if i in vowels]
        op=""
        for x in v:
            op+=x
        print(op)
        print("~~~~~~~~~~")
    def printVowel(self):
        s = "hello india"
        vowels = "aeiou"
        for i in s:
            if i in vowels:
                print(i,end="")

ob=VowelFromString()
ob.printVowelUsingLC()
ob.printVowel()