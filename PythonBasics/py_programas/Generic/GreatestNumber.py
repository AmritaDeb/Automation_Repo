a=50
b=20
c=60
d=24
if (a>=b) and (a>=c):
    x=a
elif (b>=a) and (b>=c):
    x=b
elif (c>=a) and (c>=b):
    x=c
else:
    x=d
print("Largest : ", x)