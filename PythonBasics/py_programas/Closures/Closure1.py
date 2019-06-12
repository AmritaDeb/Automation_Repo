def print_messege():
    def print_messege_inner():
        print("hello")
    return print_messege_inner
inner = print_messege()
inner()