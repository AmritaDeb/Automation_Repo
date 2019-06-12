class ColorBlue:
    def type1(self):
        print("Color Blue")
class ColorRed:
    def type2(self):
        print("Color Red")
class ColorPurple(ColorBlue,ColorRed):
    def type3(self):
        print("Combination of blue and red")
ob=ColorPurple()
ob.type1(),ob.type2(),ob.type3()