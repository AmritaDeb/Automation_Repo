#   wap to multiply 2 lists
class Multiply2List:
    def mul2List(self):
        l1=[1,2,3]
        l2=[5,4,7]
        d=dict()
        l = list(map(lambda m, n: m * n, l1, l2))
        print(list(l))

ob=Multiply2List()
ob.mul2List()