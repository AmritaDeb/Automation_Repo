#   wap to create a list of tuples with the 1st element as the number and 2nd element as the square as the number
class ListOfTuple:
    def listOfTuple(self,l1):

        l2=map(lambda l1:l1**2,l1)
        print(list(l2))

        l3=[i**2 for i in l1]
        print(l3)

        d={x:y for x,y in zip(l1,l3)}
        print(d.items())

ob=ListOfTuple()
l1=[1,2,3,4,5]
ob.listOfTuple(l1)
