"""
1. User must enter the number of elements in the list and store it in a variable.
2. User must enter the values to the same number of elements into the list.
3. The append function obtains each element from the user and adds the same to the end of the list as many times as the number of elements taken.
4. The same of 2 and 3 is done for the second values list also.
5. The two lists are merged together using the zip() function.
6. The zipped lists are then merged to form a dictionary using dict().
7. The dictionary formed from the two lists is then printed.
"""
keys=[]
values=[]
n=int(input("Enter number of elements for dictionary:"))
print("For keys:")
for x in range(0,n):
    element=input("Enter element" + ":")
    keys.append(element)
print("For values:")
for x in range(0,n):
    element=int(input("Enter element" + ":"))
    values.append(element)
# The zipped lists are then merged to form a dictionary using dict().
d=dict(zip(keys,values))
print("The dictionary is:")
print(d)
