l1=[1,2,3,4]
l2=[10,20,30,40]
"""
ADDITION:
1. append(value) 
2. extend(value)
3. insert(position,value)
"""
l1.append('hello')
print(l1)
l1.append(l2)
print(l1)
l1.extend(l2)
print(l1)
l1.insert(2,'hi')
print(l1)

"""
1. count(value)
2. rwverse()
3. index(value)
"""
print(l1.count(10))
l1.reverse()
print(l1)
print(l1.index(30))

"""
1. sort()
2. sorted(value)
"""
# l1.sort()
# print(l1)
# print(sorted(l1))

"""
DELETION:
1. pop()
2. remove(value)
3. clear()
"""
l1.pop()
print(l1)
l1.remove('hi')
print(l1)
l1.clear()
print(l1)

"""
SLICING
"""
Day=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
Day[1:3]=['Monday','Tuesday']
print(Day)

"""
Built-in:
1. len()
2. max()
3. min()
4. sorted()
5. sum()
"""
x=[1,20,10,8,5]
print(len(x))
print(max(x))
print(min(x))
print(sorted(x))
print(sum(x))