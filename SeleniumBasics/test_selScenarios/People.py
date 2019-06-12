class Person(object):
    def __init__(self,name,fav_animal=None):
        self.name=name
        self.fav_animal=fav_animal

def dogs(People):
    return any(
        [p.fav_animal=="dog" for p in People]
    )

ob=Person("Amy")
ob1=Person("amrita","birds")
ob2=Person("sid","dog")
