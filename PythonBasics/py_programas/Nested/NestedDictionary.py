employees={1:{'name':'Amrita','age':24,'sex':'F'},
              2:{'name':'Sid','age':25,'sex':'M'}}
print(employees)     #{1: {'name': 'Amrita', 'sex': 'F', 'age': 24}, 2: {'name': 'Sid', 'sex': 'M', 'age': 25}}
print(employees[1])  #{'name': 'Amrita', 'sex': 'F', 'age': 24}
print(employees[2])  #{'sex': 'M', 'name': 'Sid', 'age': 25}

for id in employees:
    if employees[id]['name'] == 'Amrita':
        print(employees[id]['age'])
