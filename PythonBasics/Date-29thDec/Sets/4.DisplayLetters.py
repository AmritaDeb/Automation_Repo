#   wap that displays which letters  are present in both the string
class DisplayLetters:
    def display(self):
        s1 = input("Enter the first string:")
        s2 = input("Enter the first string:")
        print(set(s1).intersection(set(s2)))
ob=DisplayLetters()
ob.display()