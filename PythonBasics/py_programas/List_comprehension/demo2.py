n=[1,2,3,4,5]
A=[i for i in range(1,6)]
print((list(A)))

l1=['a','b','c','d']
l2=[9,8,7,6]
d={x:y for x,y in zip(l1,l2)}
print(d)

l3=[9,8,7,6]
d2={v:v*2 for v in l3 if v%2==0}
print(d2)
