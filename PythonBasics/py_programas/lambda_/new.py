a = [2,3,5,4,8,9,7]
A=list(filter(lambda x:x%2==0,a))
print(A)

M=list(map(lambda x:x%2==0,a))
print(M)

B=list(filter(lambda x:x**2,a))
print(B)

M=list(map(lambda x:x**2,a))
print(M)