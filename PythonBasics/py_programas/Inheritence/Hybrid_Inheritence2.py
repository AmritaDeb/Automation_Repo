class Rainbow:
    def type(self):
        print("Combination of 7 colors")
class ColorBlue(Rainbow):
    def type1(self):
        print("Color blue is Inherited from Rainbow")
class ColorRed(Rainbow):
    def type2(self):
        print("Color Red is inherited from Rainbow")
class ColorPurple(ColorBlue,ColorRed):
    def type3(self):
        print("Combination of blue and red")
ob=ColorPurple()
ob.type3(),ob.type2(),ob.type1(),ob.type()