names1 = {'John', 'Marry', 'Lena', 'Pollux'}
names2 = {'Dan', 'Arthur', 'Marry', 'Lena', 'Castor'}

# Using set methods create a list called names that contains the elements that belong to both sets
# names will be  ['Lena', 'Marry']

# YOUR CODE STARTS HERE
names = list(names1 & names2)
print(names)
