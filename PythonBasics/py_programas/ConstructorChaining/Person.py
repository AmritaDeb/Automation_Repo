class Person:
    def __init__(self,name):
        self.name=name
        print(self.name)

class College:
    def __init__(self,name,location):
        Person.__init__(self,name)
        self.location=location
        print(self.location)

print("Within same class:")
x=Person("Amy")
print("Has a relationship:")
y=College("Sonu",18)
print(type(x))
