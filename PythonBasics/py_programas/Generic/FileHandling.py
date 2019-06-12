"""f=open("file1.txt","w")
data="good morning"
f.write(data)
print("Success")
f.close()"""
f=open("file1.txt","r")
data=f.read()
print("The retrieved data is : ",data)
print(f.readline())
print(f.read(7))
