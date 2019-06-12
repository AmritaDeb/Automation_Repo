def greet(a):
    def inner():
        print("whats your name?")
        a()
        print("end")
    inner()
@greet
def display():
    print("hi")