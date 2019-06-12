import json
data={'a':'apple','b':'bat'}
file = open("write_data_json.txt","w")
JSData = json.dumps(data)
file.write(JSData)

