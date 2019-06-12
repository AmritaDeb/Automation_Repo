#   wap to read the content of a file in reverse order
class ReadFileInReverse:
    def readInReverse(self):
        with open("readdata.txt","r") as file:
            for line in reversed(list(file)):
                print(line.rstrip())
ob=ReadFileInReverse()
ob.readInReverse()