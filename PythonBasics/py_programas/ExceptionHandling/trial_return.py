n1=51
n2=0
def trial():
    try:
        c=n1/n2
        return "The result is:",c
    except ZeroDivisionError:
        return "Invalid"
    except Exception:
        return "Supermost exception"
    finally:
        return "its a finally block"
print(trial())
