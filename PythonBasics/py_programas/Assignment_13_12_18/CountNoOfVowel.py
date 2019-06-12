ip=input("Enter the String: ")
count=0
vowel=set("aeiou")
for letter in ip:
    if letter in vowel:
        count+=1
print("Total count of voewels: ",count)
