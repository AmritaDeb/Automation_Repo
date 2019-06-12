from functools import partial

def multiplier(x, y):
    return x * y

multiplier_partials = []
for i in range (1, 11):
    function = partial(multiplier, i)
    multiplier_partials.append(function)

print(multiplier_partials[0](2))
print(multiplier_partials[1](5))