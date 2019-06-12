#   wap to stop the Iteration using raise
class StopException(Exception):
    pass

class CheckStopIter():
    n=int(input("number less than 999 at which have to throw an exception "))
    for i in range(1000):
        if i>n:
            raise StopException
        else:
            print(i)

ob=CheckStopIter