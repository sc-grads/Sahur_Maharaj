import csv

with open('passwd.csv') as f:
    reader = csv.reader(f, delimiter=':', lineterminator='\n')
    for r in reader:
        print(r)

# dialects
print(csv.list_dialects())
csv.register_dialect('hashes', delimiter='#', quoting=csv.QUOTE_NONE, lineterminator='\n')
with open('items.csv') as f:
    read = csv.reader(f, dialect='hashes')
    for r in read:
        print(r)

