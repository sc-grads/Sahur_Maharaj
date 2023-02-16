# High order function
import math


def sum(n, fn):
    res = 0
    for i in range(1, n + 1):
        res += fn(n)

    return res


def sqare(x):
    return x ** 2


print(sum(3, sqare))

res = sum(3, math.sqrt)
print(res)


# functions creturning a function
def cpute(msg):
    if msg == 'square':
        return sqare
    else:
        return math.sqrt


func = cpute('square')
print(func(10))

# functions can be nested
def outer():
    msg = 'Python'
    x = 0

    # defining an inner function
    def inner():
        # nonlocal is used to declare that a variable inside a nested function
        # is not local to it (it lies in the outer enclosing function).
        nonlocal x  # this is `x` from outer function
        x += 1
        print(f'{msg} is really cool!')  # `msg` and `x` are free variables
        return x

    return inner


func1 = outer()
print(type(func1))  # => <class 'function'>

xx = func1()
print(xx)  # => 1

print(func1())  # => 2
print(func1())  # => 3


# Decorators
user = {'usrname': '123', 'lvl': 'admin'}

def only_admin(fn):
    def wrapper_only_admin(*args, **kwargs):
        if user['lvl'] == 'admin':
            return fn(*args, **kwargs)
        else:
            raise PermissionError('Error')
    return wrapper_only_admin

def rm_file(f=None):
    import os, os.path
    if os.path.isfile(f):
        os.remove(f)
        print(f"removed: {f}")
    else:
        print('FNE')

remove_file = only_admin(rm_file)
remove_file('a.txt')



def permission(func):
    if user['lvl'] == 'admin':
        return func
    else:
        return None

def show_pass():
    return 'rgezssshg'

fn = permission(show_pass)
if fn != None:
    print(fn())
else:
    print('Cannot run function')