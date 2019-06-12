#   wap to count the number of lines in a text file
class CountNoOfLines:
    def countNoOfLines(self):
        num_lines=0
        with open("readdata.txt","r") as file:
            for line in file:
                num_lines+=1
        print("Number of lines: ", num_lines)
ob=CountNoOfLines()
ob.countNoOfLines()