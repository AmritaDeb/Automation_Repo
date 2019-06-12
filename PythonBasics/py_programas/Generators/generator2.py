def reverseString(str):
    for i in range(len(str)-1,-1,-1):
        yield str[i]
l=[]
for char in reverseString("amrita"):
    l.append(char)
    print(char)

print(l)
