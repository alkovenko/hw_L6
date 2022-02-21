def concat(*args, reversed=False):
    my_string = ''
    if reversed == False:
        for word in args:
            my_string += str(word)
        return my_string
    else:
        for word in args[::-1]:
            my_string += str(word)
        return my_string

print(concat('Hello', ' ', 'world', reversed=True))