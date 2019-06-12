class decorator2():

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Entering", self.f.__name__)
        self.f()
        print("Exited", self.f.__name__)

@decorator2
def func1():
    print("inside func1()")

@decorator2
def func2():
    print("inside func2()")

func1()
func2()