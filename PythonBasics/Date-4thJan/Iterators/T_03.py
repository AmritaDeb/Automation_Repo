class OddNum:

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num

i=iter(OddNum())
for j in range(25):
    print(next(i))