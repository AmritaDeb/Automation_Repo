import json
file = open("data.txt","r")
data = file.read()
JSData = json.loads(data)
print(JSData)
print(JSData.get('a'))