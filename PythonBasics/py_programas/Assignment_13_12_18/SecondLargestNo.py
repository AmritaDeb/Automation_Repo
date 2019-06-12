class SecondLargest:
    def secondLargest(self):
        n = int(input("Enter the no of elements: "))
        b = []
        for i in range(n):
            a = int(input("Enter the element:"))
            b.append(a)
        b.sort()
        # b.reverse()
        # print("The second largest no: ", b[1])
        print("The second largest no: ", b[-2])
ob=SecondLargest()
ob.secondLargest()