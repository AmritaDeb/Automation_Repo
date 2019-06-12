from PythonBasics.py_programas.ExceptionHandling import AgeInvalidException
class dem:
    age=int(input("Enter your age : "))
    if (18<=age):
        print("Eligble")
    else:
        raise AgeInvalidException


