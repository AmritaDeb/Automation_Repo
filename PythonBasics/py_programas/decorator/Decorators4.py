
def make_decorated(f):
    def inner_func(k):
        print("Value of", k , " :" )
        return f(k)
    return inner_func

@make_decorated
def get_value(given_key):
    dict = {'a' : 'apple', 'm' : 'mango'}
    for key,value in dict.items():
        if given_key == key:
            return value
        return "key does not exist"

print(get_value('a'))
print(get_value('c'))






