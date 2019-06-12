l=[10,20,30,40,50]
i = iter(l)
for a in l:
    print(next(i))

x = l.__iter__()
for b in range(6):
    print(x.__next__())