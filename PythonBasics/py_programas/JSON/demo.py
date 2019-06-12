import json
f = open("data.txt","w")
data={'a':'apple','b':'bat'}
JSdata = json.dumps(data)
f.write(JSdata)
print("successfully")
f.close()