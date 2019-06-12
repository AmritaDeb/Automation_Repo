class Demo:
    a=10
    def __init__(self):
        print("constructor")
    def fun(self):
        print(self.a)
    @classmethod
    def fun1(cls):
        print(cls.a)

ob=Demo.fun1()
ob=Demo.fun()
