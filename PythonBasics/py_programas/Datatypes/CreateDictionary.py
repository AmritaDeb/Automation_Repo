class Test:
    # empty dictionary
    my_dict = {}
    print(my_dict)                          # {}

    # dictionary with integer keys
    my_dict = {1: 'apple', 2: 'ball'}
    print(my_dict)                          # {1: 'apple', 2: 'ball'}

    # dictionary with mixed keys
    my_dict = {'name': 'John', 1: [2, 4, 3]}
    print(my_dict)                          # {1: [2, 4, 3], 'name': 'John'}

    # using dict()
    my_dict = dict({1: 'apple', 2: 'ball'})
    print(my_dict)                          # {1: 'apple', 2: 'ball'}

    # from sequence having each item as a pair
    my_dict = dict([(1, 'apple'), (2, 'ball')])
    print(my_dict)                          # {1: 'apple', 2: 'ball'}