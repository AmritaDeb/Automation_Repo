class LeapYear:
    def leapYr(self):
        yr=int(input("Enter the year: "))
        if yr%4==0:
            print("{0} is a leap year".format(yr))
        else:
            print("{0} is not a leap year".format(yr))
ob=LeapYear()
ob.leapYr()
