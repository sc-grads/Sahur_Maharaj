def vowel_count(my_str):
    """
    This function counts the number of vowels in a string and returns a dictionary.
    """
    vowels = 'aeiou'

    ## YOUR CODE STARTS HERE
    my_str = my_str.lower()
    sentance = dict()
    for c in my_str:
        if c in vowels:
            if c in sentance.keys():
                sentance[c] += 1
            else:
                sentance[c] = 1
    return sentance


print(vowel_count('The quick brown fox jumped over the lazy dog'))