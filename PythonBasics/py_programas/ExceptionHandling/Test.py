# n1=int(input("Enter the 1st number: "))
# n2=int(input("Enter the 2nd number: "))

n1=51
n2=2
def trial():
    try:
        c=n1/n2
        print("The result is:",c)
    except ZeroDivisionError:
        print("Invalid")
    except Exception:
        print("Supermost exception")
    finally:
        print("its a finally block")
    print("end")
trial()
