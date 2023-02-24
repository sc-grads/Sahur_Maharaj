# Functions used to reapeat code and add modularity
def my_funct():
    print('Hello py 1')
    x = 10
    print(x ** 10)


# functions wont run unless called
my_funct()  # <-- function called and will run

# docstrings
print(len('Python is coool'))  # hover for builtin help


def say_hi(name):
    """This Function says hello your name"""  # <-- documentation string for func explanation.
    print(f'Hello {name}!!!!')


say_hi('Shay')  # <--hover over for docstr
help(say_hi)
print(say_hi.__doc__)


# positonal args
# key word args ignore order of positional
# def args
# *args
# **kwargs

def diffr(a, b):
    return a - b


x = diffr(1, 5)
print(x)


def func1(x, y, z):  # <-- params local to function
    print(f'X: {x}')
    print(f'Y: {y}')
    print(f'Z: {z}')


# func1(1, 555)  # <-- arguments
func1(y=1, z=50, x=1023)  # keyword args


# default args positionals must have default values afte
def add(x, y=10, z=222):  # set def var for y

    print(f'x is: {x}\ny is: {y}\nz is: {z}')
    print(f'Sum: {x + y + z}')


add(2, 4)

add(x=120, z=55)

# return  --> ses functions to values
n = len([1, 2, 4, 5])  # len retunrns value in len n


# variable len args - *args  <-- tuple of potential arguments
def avg(a, b, *args):
    print(f'Aargs are: {args}')
    return (a + b) / (2 + len(args))


print(avg(4, 5, 6, 7, 8, 9, 45, 2))


# **kawargs dictionary of positional args
def myfunc(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(f'key: {k}\nvalue: {v}')


myfunc(name='hi', age=32, student=True)


# lambda expressions anony funcs
# lambda param key func

def add(a,b,c):
    res = a + b + c
    return res

# lambda
var = (lambda a, b, c: a + b + c)(3, 4, 5)
print(var)

powr_2 = (lambda x: x**2)
print(powr_2(3))



