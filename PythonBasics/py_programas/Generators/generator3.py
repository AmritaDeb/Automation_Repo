def demo_generator(l):
    l1=[]
    for i in l:
        l1.append(i**2)
        yield l1
l=[1,2,3,4]
for item in demo_generator(l):
    print(item)
