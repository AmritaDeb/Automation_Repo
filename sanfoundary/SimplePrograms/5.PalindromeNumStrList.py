def reverseNum(num):
    rev=0;temp=num
    while num>0:
        dig=num%10
        rev=rev*10+dig
        num//=10
    if rev==temp:
        print("The number is Palindrome")
    else:
        print("The number is not Palindrome")

def reverseStr(str):
    if str==str[::-1]:
        print("The string is Palindrome")
    else:
        print("The string is not Palindrome")

def reverseList(li):
    if li==li[::-1]:
        print("The list is Palindrome")
    else:
        print("The list is not Palindrome")

reverseNum(1001)
reverseStr("amrita")
reverseList([4,2,2,4])