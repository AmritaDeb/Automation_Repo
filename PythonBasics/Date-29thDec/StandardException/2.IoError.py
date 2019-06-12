#   wap for io error
def ioError():
    try:
        f = open("test.txt", 'r')
        f.write("Hi")
    except Exception as e:
        print(type(e))
ioError()