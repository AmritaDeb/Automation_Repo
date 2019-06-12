d={'a':30,'b':50,'c':20,'d':30}
l=d.values()
print(l)
l1=set(l)
print(l1)

s="amrita"
s1=" "
l=list(s)
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
s1=str(l1)
print(s1)
