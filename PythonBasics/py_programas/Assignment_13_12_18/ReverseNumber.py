class Reverse:
    def reverse(self):
        n = int(input("Enter number: "))
        rev = 0
        # while (n > 0):
        for i in range(n):
            if self.digitCount(n)==0:
                break
            else:
                dig = n % 10
                rev = rev * 10 + dig
                n = n // 10
        print("Reverse of the number:", rev)
    def digitCount(self,n):
        count = 0
        while n > 0:
            n=n//10
            count=count+1
        return count
ob=Reverse()
ob.reverse()