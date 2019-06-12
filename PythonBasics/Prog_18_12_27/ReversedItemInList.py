l1=['hi','hello','bye']
l2=[]
for i in range(len(l1)):
    l2.append(l1[i][::-1])
print(l2)

s="hello"
print("".join(reversed(s)))
