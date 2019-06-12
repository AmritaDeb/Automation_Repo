class Rice:
    def type(self):
        print("Basmati Rice")
class WhiteRice(Rice):
    def type1(self):
        print("Cooked white rice")
class GheeRice(Rice):
    def type2(self):
        print("Cooked ghee rice with kaju and masala")
class FriedRice(WhiteRice,GheeRice):
    def type3(self):
        print("Combination of WhiteRice and GheeRice is FriedRice")
ob=FriedRice()
ob.type(),ob.type1(),ob.type2(),ob.type3()

"""Output
Basmati Rice
Cooked white rice
Cooked ghee rice with kaju and masala
Combination of WhiteRice and GheeRice is FriedRice
"""