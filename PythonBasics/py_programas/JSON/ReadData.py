import json
f=open("data.txt","r")
JSdata = json.load(f)
print("Retrieve data",JSdata)
f.close()