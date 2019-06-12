#   wap to raise a type error if the input is not an integer
class RaiseTypeError:
    def raiseTypeError(self,n):
        if n.isdigit():
            pass
        else:
            print("entered number is not an integer")
            raise TypeError

ob=RaiseTypeError()
n = input("enter a number")
ob.raiseTypeError(n)
