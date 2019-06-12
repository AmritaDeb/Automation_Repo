#   wap to map 2 lists into a dictionary
class Map2ListInDict:
    def map2List(self):
        l1=[1,2,3]
        l2=[5,4,7]
        d=dict()
        # op=map(lambda x,y:x+y,l1,l2)
        op={x:y for x,y in zip(map(int,l1),map(str,l2))}
        print(op)

ob=Map2ListInDict()
ob.map2List()