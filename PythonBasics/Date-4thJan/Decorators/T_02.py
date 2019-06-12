def entry_exit(f):
    def learn():
        print("Entering", f.__name__)
        f()
        print("Exited", f.__name__)
    return learn

@entry_exit
def school():
    print("inside school()")

@entry_exit
def office():
    print("inside office()")

school()
office()
print(office.__name__)