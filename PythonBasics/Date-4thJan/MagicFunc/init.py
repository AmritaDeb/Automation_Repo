class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def __call__(self,name,age):
        super().__init__(name,age)
        print("employee method")
class Student(Person):
    def __init__(self,name,age):
        super().__init__(name,age)

Emp1=Employee("Amrita",50)
Emp2=Employee("Arpita",15)
print(Emp1.name,Emp1.age)
print(Emp2.name,Emp2.age)