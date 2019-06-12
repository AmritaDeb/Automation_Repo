
def make_decorated(f):
    def inner_func(x,y):
        print("Start")
        return f(x,y)
    return inner_func

@make_decorated
def add_func(a,b):
    return a+b

print(add_func(20,5))
# print(add_func(5,0))

