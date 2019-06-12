#   wap to raise an exception if the given input is below zero
class RaiseBelowZeroException(Exception):
    pass
class GetValue():
    n=int(input("enter a number"))
    if n<0:
        raise RaiseBelowZeroException