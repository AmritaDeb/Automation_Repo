class Human:
    def sayHello(self,name=None):
        if name is not None:
            print("Hello " + name)
        else:
            print("Hello")
ob=Human()
ob.sayHello()               # Hello
ob.sayHello("Rex")          # Hello Rex