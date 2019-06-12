#wap to append the content of 1 file into another file
class AppendContentsFromAnotherFile:
    def appendContents(self):
        fin=open("readdata.txt","r")
        data=fin.read()
        fin.close()
        fout=open("writedata.txt","w")
        fout.write(data)
        fout.close()
ob=AppendContentsFromAnotherFile()
ob.appendContents()