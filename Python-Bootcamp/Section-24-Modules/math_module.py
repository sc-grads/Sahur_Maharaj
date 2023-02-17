a = 20
def add_a(*args):
    s = 0
    for n in args:
        s += n
    return s


def sqrt(c):
    return c ** 2


if __name__ == '__main__':
    print(f'__name__ in math is: {__name__}')
