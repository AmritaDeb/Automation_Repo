import requests
import json
import jsonpath
baseURL="https://reqres.in"
res="/api/users?page=2"

response=requests.get(baseURL+res)
print(response)
print(response.content)

print(response.status_code)
assert response.status_code==200
print(response.headers)
print(response.headers.get("Date"))
print(response.headers.get("Content-Type"))
print(response.headers.get("Server"))
print(response.cookies)
print(response.encoding)
print(response.elapsed)
print(response.text)#raw format
json_response=json.loads(response.text)
print(json_response)
pages=jsonpath.jsonpath(json_response,'total_pages')

print(type(pages))#list
print(pages[0])

#assert pages[0]==5

name=jsonpath.jsonpath(json_response,'data[0].first_name')

print(name)
print(name[0])
print('------')


for i in range(0,3):
    fname = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].first_name')
    print((fname[0]))
