countries = {'us': 'United States of America', 'br': 'Brazil', 'de': 'Germany', 'at': 'Austria'}

# YOUR CODE STARTS HERE
# print out the values of the dictionary sorted by keys alphabetically. Each value should be on its own line.

sorted_keys = sorted(countries.keys())
for key in sorted_keys:
    print(countries[key])
