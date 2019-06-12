class Hotel:
    def __init__(self):
        self.index = -1
        self.menu = ['jamun', 'laddu', 'kajubarfi', 'jalebi']
    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if self.index>=len(self.menu):
            raise StopIteration
        return self.menu[self.index]
ob=Hotel()
i=iter(ob)
print(next(i))
print(next(i))
print(next(i))
print(next(i))