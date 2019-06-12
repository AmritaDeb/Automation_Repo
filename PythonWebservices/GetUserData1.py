
response=requests.get(baseURL+res)import  requests
import json
import jsonpath


baseURL="https://reqres.in"
res="/api/users?page=2"



json_response=json.loads(response.text)

lst=[10,20,30]
# print(type(lst))

# for i in range(0,3):
#     print(lst[i])


first_name = jsonpath.jsonpath(json_response, 'data[0].first_name')
print(first_name[0])

for i in range(0,3):
    fname = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].first_name')
    print((fname[0]))

