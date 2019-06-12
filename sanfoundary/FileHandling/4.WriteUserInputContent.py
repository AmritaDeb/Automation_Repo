file=open("write.txt","w")
for lines in range(2):
    file.write(input("Please enter the content:"))
    file.write("\n")
file.close()

lines=open("write.txt","r")
data = lines.read()
print(data)
