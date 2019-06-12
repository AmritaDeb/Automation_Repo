def reverseNum(num):
    rev=0;temp=num
    while num>0:
        dig=num%10
        rev=rev*10+dig
        num//=10
    print(rev)

def reverseStr(str):
    print(str[::-1])

def reverseList(li):
    print(li[::-1])


reverseNum(1024)
reverseStr("amrita")
reverseList([4,2,8,9])