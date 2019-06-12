"""
Python Program to Determine How Many Times a Given Letter Occurs in a String Recursively
"""
str="amrita"
print(str.count('a'))
print(str[1:])
print(str[0])
print(list(str))
result=[]
duplicate=[]
for s in list(str):
    if s not in result:
        result.append(s)
    else:
        duplicate.append(s)
print(result)
print(duplicate)
D = {s:str.count(s) for s in str if str.count(s)>1}
print(D)


def check(string, ch):
    if not string:
        return 0
    elif string[0] == ch:
        return 1 + check(string[1:len(string)], ch)
    else:
        return check(string[1:len(string)], ch)

string = "amrita"
ch = "a"
print("Count is:")
print(check(string, ch))