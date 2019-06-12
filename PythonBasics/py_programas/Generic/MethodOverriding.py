class Mother:
    def singing(self):
        print("Classical Singer")
class Daughter(Mother):
    def singing(self):
        print("Folk Singer")
ob=Daughter()
ob.singing()        # Folk Singer