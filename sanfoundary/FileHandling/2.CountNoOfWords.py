count=0
lines=open('read.txt','r')
for line in lines:
    words=line.split()
    count += len(words)
print(count)

fname = input("Enter file name: ")
num_words = 0
f= open(fname, 'r')
for line in f:
    words = line.split()
    num_words += len(words)
print("Number of words:")
print(num_words)