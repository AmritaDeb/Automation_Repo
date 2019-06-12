lines=open("read.txt","r")
data = lines.read()
print(data)

a=str(input("Enter the name of the file with .txt extension:"))
file2=open(a,'r')
data1=file2.read()
print(data1)
