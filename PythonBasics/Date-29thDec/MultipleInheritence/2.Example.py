class WhiteRice:
    def type1(self):
        print("Cooked white rice")
class GheeRice:
    def type2(self):
        print("Cooked ghee rice with kaju and masala")
class FriedRice(WhiteRice,GheeRice):
    def type3(self):
        print("Combination of WhiteRice and GheeRice is FriedRice")
ob=FriedRice()
ob.type1(),ob.type2(),ob.type3()