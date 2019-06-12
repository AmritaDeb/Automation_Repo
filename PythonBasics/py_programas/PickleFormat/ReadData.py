import pickle as p
f=open("demo.pkl","rb")
data=p.load(f)
print("successful")
f.close()