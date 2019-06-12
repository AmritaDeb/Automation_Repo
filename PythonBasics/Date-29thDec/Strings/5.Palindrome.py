#   wap to check if a string is a palindrome or not
def palindrome():
    str = "amrita"
    temp = str[::-1]
    if str == temp:
        print("Palindrome")

    else:
        print("Not Palindrome")
palindrome()