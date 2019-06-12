from heapq import merge
list1=list(set([1,5,4,7,5,4,2,1,6,8,9]))
list2=list(set([10,42,74,65,85,47,42,10]))
x=list(merge(list1,list2))
print(list1)
print(list2)
print(x)