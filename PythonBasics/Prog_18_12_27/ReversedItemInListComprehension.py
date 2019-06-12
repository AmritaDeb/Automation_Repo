l1=['hi','hello','bye']
l2=[]
for i in range(len(l1)):
    l2.append(l1[i][::-1])
print(l2)

revList=[l1[i][::-1] for i in range(len(l1))]
print(revList)

s="amrita"
s1=list(s)
print(s1)
# revStr=[s1[i][::-1] for i in s]
# print(revStr)