#   wap that displays which letters are in the 1st string but not in the 2nd
class DisplayLetters:
    def display(self):
        s1 = input("Enter the first string:")
        s2 = input("Enter the Second string:")
        print(set(s1) - set(s2))
ob=DisplayLetters()
ob.display()