# original = [10,20,30,20,50,10,20]
# unique = []
# duplicate = []
#
# for i in original:
#     print(original.count(i))
# L = {i:original.count(i) for i in original}
# print(L)
#
# count = 0
# c_d = {}
# for i in original:
#     if i not in unique:
#         unique.append(i)
#     else:
#         duplicate.append(i)
# print("original : ",original)
# print("unique : ",unique)
# print("duplicate : ",duplicate)

# list1 = [60,50,30,40,90,25,40]
# list2 = []
# list = list1.copy()
# min = list1[0]
# while list1:
#     for i in list1:
#         if i < min:
#             min = i
#     list2.append(min)
#     list1.remove(min)
#
# print(list)
# print(list1)
# print(list2)

data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []
original = data_list.copy()

while data_list:
    minimum = data_list[0]  # arbitrary number in list
    for x in data_list:
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)

print(original)
print(data_list)
print(new_list)

