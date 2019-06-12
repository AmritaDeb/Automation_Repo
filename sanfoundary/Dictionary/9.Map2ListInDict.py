l1=[1,2,3,4]
l2=[10,20,30,40]
d1=dict(zip(l1,l2))
print(d1)
d2={k:v for k,v in zip(l1,l2)}
print(d2)