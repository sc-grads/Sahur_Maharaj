
# List with duplicates
years = [2010, 2010, 2011, 2011, 2012, 2012, 2012]

# New list with unique elements
years_unique = []
[years_unique.append(y) for y in years if y not in years_unique]

# YOUR CODE STARTS HERE
print(years_unique)