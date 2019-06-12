from functools import partial

def find_power(a,b):
    return a**b

print(find_power(2,3))
print(find_power(4,2))

cube_num=partial(find_power,3)
print(cube_num(3))

square=partial(find_power,b=2)
print(square(6))