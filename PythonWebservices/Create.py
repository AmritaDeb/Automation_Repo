import requests
import json
import jsonpath


# baseURL="https://reqres.in"
# res="/api/users?page=2"
# file=open("./UserData.json","r")
# json_input=file.read()
# req=json.loads(json_input)
#
# print(req)
# response=requests.post(baseURL+res,req)
# print(response)
# print(response.status_code)
#
# print(response.text)
# response_json=json.loads(response.text)
# id=jsonpath.jsonpath(response_json,"id")
# print(id[0])


payload = {'page' : 2, 'count' : 25}
r = requests.get("https://httpbin.org/get",params=payload)
print(r.text)





































