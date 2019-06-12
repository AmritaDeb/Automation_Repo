import json
dict1='{"1":"Helium","2":"Lithium","3":"Berilium"}'
jsonvals=json.loads(dict1)
print(jsonvals)
print(jsonvals["1"])
print(jsonvals["2"])

for x,y in dict1:
    print (y, x)

released = {
		"iphone" : 2007,
		"iphone 3G" : 2008,
		"iphone 3GS" : 2009,
		"iphone 4" : 2010,
		"iphone 4S" : 2011,
		"iphone 5" : 2012
	}
print (released)
print(len(released))
for item in released:
    print(item)