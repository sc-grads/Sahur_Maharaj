## Defining a class
class Circle:
    def __init__(self, radius):  # instance attribute
        self.radius = radius

    ## Magic Method that is automatically called when printing an object
    def __str__(self):
        return str(self.radius)  # returning the radius as a string


## Creating an instance called moon with a radius of 1737
moon = Circle(1737)

print(moon)
