def outerM():
    print("hi")
    def innerM():
        # print("hello")
        return "hello"
    return innerM()
print(outerM())