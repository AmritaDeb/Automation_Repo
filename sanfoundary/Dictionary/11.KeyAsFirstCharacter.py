l=['apple','bannana','chiku','dragon','almond']
d1={}
for val in l:
    if val[0] not in d1.keys():
        d1[val[0]]=val
print("d1" , d1)

# d={}
# D = {w[0]:w for w in l}
# print(D)

D = {w[0]:w for w in l}
print(D)

# for word in l:
#     if word[0] not in d.keys():
#         d[word[0]] = word
# print(d)
# for word in l:
#     if(word[0] not in d.keys()):
#         d[word[0]]=[]
#         d[word[0]].append(word)
#     else:
#         if(word not in d[word[0]]):
#           d[word[0]].append(word)
# for k,v in d.items():
#         print(k,":",v)
