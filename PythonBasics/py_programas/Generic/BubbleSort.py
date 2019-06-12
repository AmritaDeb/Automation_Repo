def bubbleSort():
    l=[95,85,65,45]
    for i in range(len(l)):
        for j in range(1,len(l)):
            if i>j:
                l[i],l[j]=l[j],l[i]
            print(l)
bubbleSort()