#   python program to count the no of vowels present in a string using set
class CountNoOfVowels:
    def countNo(self,s):
        vowels = set("aeiouAEIOU")
        count = 0
        for char in s:
            if char in vowels:
                count += 1
        print("Count of vowels", count)
ob=CountNoOfVowels()
s="Hello India"
ob.countNo(s)