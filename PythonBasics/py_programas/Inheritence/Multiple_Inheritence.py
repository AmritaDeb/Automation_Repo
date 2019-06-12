class Father:
    def activity(self):
        print("Playing Tennis")
class Mother:
    def art(self):
        print("Playing Piano")
class Daughter(Father,Mother):
    def hobby(self):
        print("Dancing")
ob=Daughter()
ob.hobby(),ob.activity(),ob.art()

""" Output:
Dancing
Playing Tennis
Playing Piano
"""