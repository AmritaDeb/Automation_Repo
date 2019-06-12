class Animal:
    a=10
    __b=20
    def eat(self):
        print("Eating...")
class Dog(Animal):
    def bark(self):
        print("Barking..")
ob=Dog()
ob.eat()
ob.bark()
print(ob.a)

""" Output:
Eating..
Barking..
"""