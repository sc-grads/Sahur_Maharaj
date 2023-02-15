# It returns the number of vowels and consonants in the string as a tuple.
def counter(my_str):
    vowels = 'aeiou'

    # YOUR CODE STARTS HERE
    tot_vowels = 0
    my_str = my_str.lower()
    for v in vowels:
        tot_vowels += my_str.count(v)
    tot_consonants = len(my_str) - tot_vowels
    return tot_vowels, tot_consonants


print(counter('Helllllllooo'))