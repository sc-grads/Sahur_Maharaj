# create models of entities as software objects
# a class is a data type

from turtle import Turtle, Screen

my_screen = Screen()  # <--object
ninja = Turtle()  # <-- object
print(my_screen.canvwidth)
ninja.shape('turtle')
ninja.color('blue')

ninja.forward(100)
ninja.right(45)
ninja.forward(100)
ninja.home()

new_ninja = Turtle()
new_ninja.color('red')
new_ninja.shape('turtle')
new_ninja.penup()
new_ninja.goto(-150, 200)
new_ninja.pendown()
new_ninja.pencolor('pink')

x = 10
while x <= 50:
    new_ninja.circle(x)
    ninja.circle(x + 5)
    x += 25

my_screen.exitonclick()


# abstraction hides important code for users
# encapsulation hides variables from classes

class Robot:
    """Class implements robot"""

    def __int__(self, name, year):  # special called automatically
        self.name = name  # <-- assign params to attributes
        self.year = year

    def __del__(self):
        print('Robot Destroyed')

r1 = Robot()
r1.name = 'hello'
r1.year = 2022
print(r1.name, r1.year)
print(r1.__doc__)
print(r1.__dict__)

# destructor automaticlly called to free resources during an objects lifetime
# python has a GC filnalizer



