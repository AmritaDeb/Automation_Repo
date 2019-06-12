class Vehicle:
    def move(self):
        print("Moving..")
class Bike(Vehicle):
    def wheel(self):
        print("2wheeler")
class Car(Vehicle):
    def wheel(self):
        print("4wheeler")
ob1=Bike()
ob2=Car()
ob1.move(),ob1.wheel()
ob2.move(),ob2.wheel()

""" Output:
Moving..
2wheeler
Moving..
4wheeler
"""