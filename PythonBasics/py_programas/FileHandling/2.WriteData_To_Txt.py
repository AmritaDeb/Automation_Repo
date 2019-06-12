"""L = ["This is Delhi \n","This is Paris \n","This is London \n"]"""
data = []
for i in range(3):
    data.append(input("enter the text : ") + " \n")
print(data)
with open("writedata.txt","w") as file:
    file.writelines(data)
