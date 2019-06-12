num_lines = 0
with open("readdata.txt", 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines: ", num_lines)