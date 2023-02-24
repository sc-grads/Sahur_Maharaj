# Global variable, initialize it with whatever value you want
x = 0

def increment():
    global x
    x = x + 1


## Call the function
increment()

## Print x
print(x)




