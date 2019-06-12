#   wap to count the number of lower case characters in a string
def countLowerCase():
    str = input("Enter the string: ")
    count = 0

    for i in str:
        if (i.islower()):
            count = count + 1
    print(count)
countLowerCase()