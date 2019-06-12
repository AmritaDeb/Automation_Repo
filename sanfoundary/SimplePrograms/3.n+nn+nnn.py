"""Compute n+nn+nnn"""

n=5
temp=str(n)
t1=temp+temp
print(t1)       // 55
t2=temp+temp+temp
print(t2)       // 555
comp=n+int(t1)+int(t2)
print("The value is:",comp)     // 615