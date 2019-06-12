class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

ob=MyClass()
print(ob.method())
# print(MyClass.method())
print(ob.classmethod())
print(MyClass.classmethod())
print(ob.staticmethod())
print(MyClass.staticmethod())