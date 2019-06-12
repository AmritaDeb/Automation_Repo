#   wap which displays the letters that are not in both the strings
class DisplayLetters:
    def display(self):
        str1 = input("Enter the first string:")
        str2 = input("Enter the first string:")
        print("Letters Which are not common in two lists:", set(str1) ^ set(str2))
ob=DisplayLetters()
ob.display()