class Test:
    a=10
    def demo(self):
        global a
        print(self.a)
        a=50
        print(a)
        b = 40
        print(b)
ob=Test()
ob.demo()
