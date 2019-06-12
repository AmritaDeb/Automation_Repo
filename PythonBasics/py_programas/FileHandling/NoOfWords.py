num_words = 0
with open("readdata.txt", 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print("Number of words: ", num_words)

