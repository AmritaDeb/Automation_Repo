
def make_decorated(f):
    def inner_func():
        print("Start")
        f()
        print("End")
    return inner_func

def simple_func():
    print("I am a simple function")

simple_func()
decor = make_decorated(simple_func)
decor()

