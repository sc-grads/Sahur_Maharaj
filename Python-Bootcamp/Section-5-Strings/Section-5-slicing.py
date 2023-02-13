# slicing allows sub stirngs
movie = 'Avengers age of ultron'
print(movie[0:2])  # <-- get 0 - 2 incl excl
print(movie[2:5])  # <-- 2 to 5 incl excl
print(movie[:2])  # <-- 0 to 2 incl excl
print(movie[2:])  # <-- 2 to end

# out of range handled with no errors step defaults to 1
print(movie[0:10:2])
print(movie[::-1])  # <-- reverse string
