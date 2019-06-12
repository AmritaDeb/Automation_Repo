user_ip = input("Enter file name: ")
num_lines = 0
with open(user_ip, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines: ", num_lines)