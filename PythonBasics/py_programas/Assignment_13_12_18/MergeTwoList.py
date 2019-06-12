def mergeList():
    l1 = [1, 2, 3, 4, 5]
    l2 = [10, 20, 30]
    l1.extend(l2)
    print(l1)
    l1.sort()
    print("After Sorting: ",l1)
def nestedList():
    l1 = [1, 2, 3, 4, 5]
    l2 = [10, 20, 30]
    l1.append(l2)
    print(l1)

mergeList()
nestedList()