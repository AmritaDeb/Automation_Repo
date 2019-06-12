def avgOfNo(li):
    total = 0
    for i in li:
        total += i
    avg = total / len(li)
    print(avg)
    # another way
    print(sum(li)/len(li))

li=[2,6,8,4]
avgOfNo(li)
limit = int(input("Please enter the range of numbers in list: "))
li=[]
for i in range(limit):
    li.append(int(input("Please enter the numbers in list: ")))
print(li)

