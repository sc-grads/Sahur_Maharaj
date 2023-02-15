a = 20
def add_a(*args):
    s = 0
    for n in args:
        s = s + a
    return s


if __name__ == '__main__':
    print(f'__name__ in math is: {__name__}')