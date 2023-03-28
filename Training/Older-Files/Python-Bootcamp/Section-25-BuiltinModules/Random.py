##############################
## The random module
##############################

## Importing the module
import random

## Returns a random float between 0 included and 1 excluded
r = random.random()
print(r)  # => 0.2486797443554869

## Returns a random float in a range
r = random.uniform(5, 100)
print(r)  # => 80.8875349166217

## Returns a random integer in a range
r = random.randint(3, 80)
print(r)  # => 18

## Returns a random integer in a range (5, 80), in steps of 4
r = random.randrange(5, 80, 4)
print(r)  # => 73

## Returns a random element of a list
mylist = list('abcd12345')
r = random.choice(mylist)
print(r)  # => 'c'

## Returns a random sample from a collection
sample = random.sample(mylist, 3)  # returns 3 random items from mylist as a new list
print(sample)  # => ['3', 'd', '1'], sample is a list

random.shuffle(mylist)  # shuffles a list in place
print(mylist)  # => ['d', '2', 'a', '3', '1', 'c', '5', '4', 'b']

rand = random.SystemRandom()  # SystemRandom class provides more entropy (more randomness)
r = rand.randint(3, 10)
print(r)  # => 9