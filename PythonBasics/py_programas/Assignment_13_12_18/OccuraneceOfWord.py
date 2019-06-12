num_words = 0
word="good"
count=0
with open("readdata.txt", 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if i==word:
                count+=1
print("Number of ocuurance: ", count)