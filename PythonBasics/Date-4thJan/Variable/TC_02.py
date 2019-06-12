""" a class method to create a Person object by birth year.
    a static method to check if a Person is adult or not.
"""

from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18

person1 = Person('mayank', 25)
person2 = Person.fromBirthYear('mayank', 1993)
print(person1.age)
print(person2.age)

print(Person.isAdult(22))
print(Person.fromBirthYear('Amy',1993))