def removeDuplicate(l1):
    l2 = []
    for i in l1:
        if i not in l2:
            l2.append(i)
    print(l2)
def removeDuplicateUsingSet(l1):
    l2 = set(l1)
    print(l2)

l1 = [5, 4, 8, 6, 4, 7, 5, 2]
removeDuplicate(l1)
removeDuplicateUsingSet(l1)