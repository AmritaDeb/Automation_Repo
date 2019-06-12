import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

p = Pizza(4, ['mozzarella', 'tomatoes'])
print(p.area())
print(p.circle_area(4))