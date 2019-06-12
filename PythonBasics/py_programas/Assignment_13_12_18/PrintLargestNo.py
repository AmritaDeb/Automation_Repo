class Largest:
    def largestNo(self):
        n=int(input("Enter the no of elements: "))
        b=[]
        for i in range(n):
            a=int(input("Enter the element:"))
            b.append(a)
        c=[]
        d=[]
        for i in b:
            if i%2==0:
                c.append(i)
            else:
                d.append(i)
        c.sort()
        c.reverse()
        d.sort()
        d.reverse()
        print(c[0])
        print(d[0])
ob=Largest()
ob.largestNo()
