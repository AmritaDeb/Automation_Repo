f=open("writedata.txt","w")
data="good morning"
f.write(data)
print("Success")
f.__enter__()
data="hello"
f.write(data)
print(f.mode)
f.close()