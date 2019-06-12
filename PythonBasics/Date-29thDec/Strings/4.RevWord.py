#   wap to reverse the word of odd index in a string
def revWord():
    str="hello hi bye"
    words=str.split()
    odd=[]
    for i in range(len(words)):
        if i%2==0:
            s=words[i]
            odd.append(s[::-1])
        else:
            odd.append(words[i])
    print(odd)
revWord()