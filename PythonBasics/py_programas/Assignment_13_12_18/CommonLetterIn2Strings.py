s1="amrita"
s2="arpita"
# Intersection using List:
print(set(s1))
li=list(set(s1).union(set(s2)))
print(li)
if len(li)>0:
    print("duplicate letter is removed")
# Intersection by using Set:
op=set(s1).intersection(set(s2))
print(op)
if len(op)>0:
    print("Common Letter is present")