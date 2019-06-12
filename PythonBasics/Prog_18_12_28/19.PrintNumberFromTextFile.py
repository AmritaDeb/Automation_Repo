#   wap to read txt file and print all the numbers present in the text file
class PrintNumberFromTextFile:
    def printNumber(self):
        num=0
        with open("readdata.txt","r") as file:
            for line in file:
                words=line.split()
                for word in words:
                    for i in word:
                        if i.isdigit():
                            print(i)

ob=PrintNumberFromTextFile()
ob.printNumber()