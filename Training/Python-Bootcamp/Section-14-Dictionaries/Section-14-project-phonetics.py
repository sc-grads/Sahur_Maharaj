alphabets = dict()
with open('phonetic_alphabet.csv') as f:  # <--
    content = f.read().splitlines()
    print(content)
    for item in content[1:]:
        k, v = item.split(',')
        alphabets[k] = v
    print(alphabets)

my_str = 'HelloPython'.upper()
print(my_str, end='--> ')

for c in my_str:
    print(alphabets[c], end='\t\t')

