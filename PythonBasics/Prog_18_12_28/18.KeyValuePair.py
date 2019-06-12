class KeyValuePair:
    def keyValuePair(self,d):
        for x,y in d.items():
            print(x,":",y)
ob=KeyValuePair()
d={'k1':'v1','k2':'v2'}
ob.keyValuePair(d)