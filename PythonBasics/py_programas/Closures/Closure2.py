def multiplier_outer(m):
    def multiplier_inner(n):
        return m*n
    return multiplier_inner
test2 = multiplier_outer(2)
print(test2(5))

test3 = multiplier_outer(3)
print(test3(9))
