
def make_decorated(f):
    def inner_func():
        print("Start")
        f()
        print("End")
    return inner_func

@make_decorated
def simple_func():
    print("I am a simple function")

simple_func()

