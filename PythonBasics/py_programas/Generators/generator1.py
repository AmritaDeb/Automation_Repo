def myGenerator():
    n=1
    yield n

    n+=1
    yield n

ob = myGenerator()
print(next(ob))
print(next(ob))

for item in myGenerator():
    print(item)