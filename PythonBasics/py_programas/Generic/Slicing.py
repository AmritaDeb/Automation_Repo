class Slicing:
    data=("a", "b", "c", "d", "e", "f", "g", "h")
    x=slice(3,5)
    print(data[x])              # ('d', 'e')
    print(data[slice(3)])       # ('a', 'b', 'c')
    print(data[slice(3,5)])     # ('d', 'e')
    print(data[slice(1,7,2)])   # ('b', 'd', 'f')
    print(data[slice(1,7,3)])   # ('b', 'e')
