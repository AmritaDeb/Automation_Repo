d={1: 'hello', 2: 'python', 3: 'world'}
print(d.get(2))
print(d.get(5))
print(d[2])
# print(d[5])
if d.get(5)!= None:
    print("Key is exist")
else:
    print("Key does not exist")

d2={'a':'apple','b':'bannana','c':'chiku'}
key = input("Enter the key : ")
if key in d2.keys():
    print("Key is exist")
    print(d2[key])
else:
    print("Key does not exist")