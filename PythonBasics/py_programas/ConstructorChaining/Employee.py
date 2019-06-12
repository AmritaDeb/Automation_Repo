class Company:
    def __init__(self,user_id):
        self.userid=user_id

class UserLogin:
    def __init__(self,name,password):
        self.name=name
        self.password=password

class UserDetails(Company):
    def __init__(self,user_id,name,password,age,loc):
        super().__init__(user_id)
        UserLogin.__init__(self,name,password)
        self.age=age
        self.loc=loc
        print("id:",user_id,"||","name:", name,"||","password:",password,"||","age:",age,"||","loc:",loc)
ob=UserDetails('321','Amy','@2541',24,'kol')

