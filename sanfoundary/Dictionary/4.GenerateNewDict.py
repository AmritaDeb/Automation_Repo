# d1={}
#
# for i in range(3):
#     key=int(input("Enter the key : "))
#     value=key*key
#     d1.update({key:value})
# print(d1)
#
# d2={}
# l=[]
# for i in range(3):
#     k=int(input("Enter the key : "))
#     l.append(k)
# d2={k:k*k for i in l}
# print(d2)

n=int(input("Enter a number:"))
d={x:x*x for x in range(1,n+1)}
print(d)