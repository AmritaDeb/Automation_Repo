def entry_exit(f):
    def learn():
        print("Entering", f.__name__)
        f()
        print("Exited", f.__name__)
        learn.__name__=f.__name__
    return learn

@entry_exit
def school():
    print("inside school()")

school()
print(school.__name__)