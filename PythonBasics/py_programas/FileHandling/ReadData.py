count=0
f=open("readdata.txt","r")
data=f.read()
print("The retrieved data is : ",data)
for line in f:
    words=line.split()
    count+=len(words)
print(count)
f.close()

num_lines = 0
with open("readdata.txt", 'r') as f:
    for line in f:
        words = line.split()
        num_lines += len(words)
print("Number of words: ", num_lines)