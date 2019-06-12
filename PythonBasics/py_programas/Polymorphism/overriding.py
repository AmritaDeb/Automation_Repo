class Mother:
    def __init__(self, age):
        self.age = age
    def working(self):
        print("Cooking")
    def working(self):
        print("Washing")
class Daughter(Mother):
    def __init__(self, mom_age, name):
        super().__init__(mom_age)
        self.name = name
    def working(self):
        print("Eating")

ob = Daughter(25,'Amy')
ob.working()
print(ob.age, ob.name)