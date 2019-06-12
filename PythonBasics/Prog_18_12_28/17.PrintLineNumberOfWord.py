#   wap to print the line numbers of a particular word
class PrintNumberFromTextFile:
    def printNumber(self,searchWord):

        with open("readdata.txt","r") as file:
            num_line = 1
            for line in file:
                if searchWord in line:
                    print(num_line)
                num_line+=1

ob=PrintNumberFromTextFile()
searchWord="good"
ob.printNumber(searchWord)