line_count = 0
word_count = 0
str_count = 0
letter_count = 0
with open("readdata.txt","r") as file:
    for line in file:
        line_count += 1
        word = line.split()
        print(word)
        word_count += len(word)
        for str in word:
            if str == "Hello":
                str_count += 1
        for str in word:
            for letter in str:
                if letter == "l":
                    letter_count += 1


print(line_count)
print(word_count)
print(str_count)
print(letter_count)

