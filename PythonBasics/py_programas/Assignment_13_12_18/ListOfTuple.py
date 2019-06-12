def listOfTuple():
    a=[(i,i**2) for i in range(1,5)]
    print(a)
    b = [(i,i**2) for i in range(1,5) if i!=1]
    print(b)
listOfTuple()