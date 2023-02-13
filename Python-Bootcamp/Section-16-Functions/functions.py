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

