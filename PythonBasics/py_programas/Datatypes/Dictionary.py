# d1 = {x:x**2 for x in range(5) if x>1}
# print(d1)

# x=['a','b','c','d']
# y=[10,20,30,40]
# d2 = {x:y for x,y in zip(x,y)}
# print(d2)

str = "amrita"

# d3 = {x.upper():x*3 for x in str}
# print(d3)
# d4 = {x:x*3 for x in str}
# print(d4)

l = list(str)
d5 = {x: l.count(x) for x in l}
print(d5)
d6 = {x: l.count(x) for x in l if l.count(x)>1}
print(d6)

# D = {'d': 'dragon', 'a': 'apple', 'b': 'bannana', 'c': 'chiku'}
# print(D.items())
# print(D.keys())
# print(D.values())
# D.update({'f':'fan'})
# print(D)
# print(D.get('c'))
# print(D['c'])
# print(D.get('e'))
# # print(D['e'])     //it will return KeyError
# D.pop('c')
# print(D)
# D.popitem()
# print(D)
# D.popitem()
# print(D)
# D.clear()
# print(D)
