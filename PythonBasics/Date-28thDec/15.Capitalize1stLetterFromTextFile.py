#   wap to read file and capitalize the 1st letter of every word in the file
class Capitalize1stLetterFromTextFile:
    def capitalize(self):
        with open("readdata.txt","r") as file:
            for line in file:
                words=line.split()
                for word in words:
                    print(word.capitalize())


ob=Capitalize1stLetterFromTextFile()
ob.capitalize()