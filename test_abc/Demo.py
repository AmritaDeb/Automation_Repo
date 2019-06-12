from datetime import date
today = date.today()
print(today)
d = today.strftime("%m_%d_%y")
print(d)