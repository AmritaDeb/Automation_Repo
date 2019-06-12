class myIterator:
    def __init__(self):
        self.index = -1
        self.menu = ['jamun','laddu']
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index >= len(self.menu):
            raise StopIteration
        return self.menu[self.index]

ob = myIterator()
i = iter(ob)
print(next(i))