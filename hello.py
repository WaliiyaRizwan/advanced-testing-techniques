def addthis(x,y):
    import pdb;pdb.set_trace()
    print(f"This is x {x} and this y {y}")
    result = x+y
    print(f"This is the result {result}")


    try:
        result = x+y
    except TypeError:
        print(f"The wrong type passed")
        result = int(x) + int(y)
    return result


print(addthis("1",2))

