a=[10,20,40,60]
for i in a:
    print(i)
i=iter(a)
print(i)
for x in range(4):
    print(next(i))
# print(next(i))        //StopIteration
