animals = ['Cat', 'Dog']

###### YOUR CODE STARTS HERE


## 1. Add an element at the end of the list. The new element will be the string 'Donkey'.
animals.append('Donkey')
## animals will be ['Cat', 'Dog', 'Donkey']
print(animals)



##2. Add an element at position 2. This will be the 2nd element and will store the string 'Horse'
animals.insert(1, 'Horse')
## animals will be ['Cat', 'Horse', 'Dog', 'Donkey']
print(animals)



##3. Return the index of the element with value 'Cat' in variable called cat_index
cat_index = animals.index('Cat')
print(cat_index)



##4. Create a string variable named str_animals from the list by joining the elements of the list using '-' as a delimiter.

## str_animals will be 'Cat-Horse-Dog-Donkey'
str_animals = '-'.join(animals)
print(str_animals)
