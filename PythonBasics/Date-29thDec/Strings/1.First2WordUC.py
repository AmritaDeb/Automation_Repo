# wap to the 1st two word of the input should be in upper case
class First2WordUC:
    def convert(self):
        str = input("Enter the string: ")
        wrd = str.split()
        count = 0
        for i in wrd:
            print(i.upper())
            count += 1
            if count > 1:
                break
ob=First2WordUC()
ob.convert()