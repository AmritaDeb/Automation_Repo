class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def margherita(cls):
        return "It's Margherita",cls(['mozzarella', 'tomatoes'])

    @classmethod
    def peppyPaneer(cls):
        return "It's Peppy Paneer",cls(['mozzarella', 'tomatoes', 'paneer'])

print(Pizza.margherita())
print(Pizza.peppyPaneer())