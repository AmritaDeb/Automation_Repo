import pickle as p
f=open("demo.pkl","wb")
data=[1,2,'hi','hello']
p.dump(data,f)
print("successful")
f.close()