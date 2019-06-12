
def greet(a):
    def inner():
        print("start")
        a()
        print("end")
    inner()
@greet
def test():
    print("hi")

