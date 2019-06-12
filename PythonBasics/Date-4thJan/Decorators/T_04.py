class my_decorator():

    def __init__(self, f):
        print("from __init__()")
        f() # Prove that function definition has completed

    def __call__(self):
        print("from __call__()")

@my_decorator
def aFunction():
    print("inside aFunction()")

print("Finished decorating aFunction()")

aFunction()