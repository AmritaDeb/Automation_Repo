#   wap for zerodivisionerror
def zeroDivisionerror():
    try:
        number = int(input("Enter the number"))
        res = number / 0
        print(res)
    except Exception as e:
        print(type(e))
zeroDivisionerror()