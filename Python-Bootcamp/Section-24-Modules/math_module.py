a = 20
def add_a(*args):
    s = 0
    for n in args:
        s = s + a
    return s