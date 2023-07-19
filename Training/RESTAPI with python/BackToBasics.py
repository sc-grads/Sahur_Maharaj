# variables
x = 15
price = 9.99
discount = 0.2
result = price * (1 - discount)
print(result)
# string and reassign
name = "ROlf"
name = "Bob"
print(name)
print(name * 2)
a = 25
b = a
print(f'b = {b}') # <--- 25
b = 12
print(a)
print(b)


# String formatting
name = 'bob'
greeting = 'hello'
usergreeting = f'{greeting} {name}'
print(usergreeting)

newgreet = 'new hello, {}'
with_name = newgreet.format(name)
print(with_name)

# input
username = input('What is the name: ') # <--- always str so convert int(), float()
print(username)

# first app
user_age = int(input('Enter Age: '))
months = user_age * 12
seconds = user_age * 365.25 * 24 * 60 * 60
print(f'Age in months {months}\nin seconds: {seconds}')

# lists tups sets
l = [1, 2, 'hello'] # <-- list
t = (1, 2, 'hello') # <-- tupple non modifyble
s = {'h1', 1, 22, 1} # <-- set no duplicate no order

print(l[0], t[0]) # access elements
l[0] = 'sds'
print(l) # change value
l.append(11)
print(l) # add value to end
l.remove(2)
s.add('aa')
print(s) # add to set











