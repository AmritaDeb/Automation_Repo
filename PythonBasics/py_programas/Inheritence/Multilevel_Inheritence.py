class Animal:
    def eat(self):
        print("Eating...")
class Dog(Animal):
    def bark(self):
        print("Barking..")
class Puppy(Dog):
    def weep(self):
        print("Weeping..")
ob1=Dog()
ob2=Puppy()
ob1.eat(),ob1.bark()
ob2.eat(),ob2.weep()


""" Output:
Eating..
Barking..
Eating..
Weeping..
"""