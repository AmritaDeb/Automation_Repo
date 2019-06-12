def evenAndOdd():
    l1=[1,5,7,8,6,4,2,3,4]
    even=[]
    odd=[]
    for i in l1:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print("Even List: ", even)
    print("Odd List:", odd)
    Even = [i for i in l1 if i%2==0]
    Odd = [i for i in l1 if i%2!=0]
    print("List Comprehension")
    print(Even,Odd)
evenAndOdd()

