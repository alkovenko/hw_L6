def concat(*args: str, reversed: bool = False):
    my_string = ''
    if reversed:
        for word in args[::-1]:
            my_string += word
    else:
        for word in args:
            my_string += word
    return my_string
