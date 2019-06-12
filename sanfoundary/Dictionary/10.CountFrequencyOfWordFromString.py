s="I am Amy. I love programming."
l=[]
l=s.split()
result={i:l.count(i) for i in l}
print(result)
duplicate={i:l.count(i) for i in l if l.count(i)>1}
print(duplicate)
