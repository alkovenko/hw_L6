def inspect(f):
    def foo(*args, **kwargs):
        print(f'Args: {args}')
        print(f'Kwargs: {kwargs}')
        out = f(*args, **kwargs)
        print(f"Retvalue: '{out}'")
        return out
    return foo

@inspect
def concat(*args: str, reversed: bool = False):
    my_string = ''
    if reversed:
        for word in args[::-1]:
            my_string += word
    else:
        for word in args:
            my_string += word
    return my_string

print(concat('hello', ' ', 'world', reversed=True))