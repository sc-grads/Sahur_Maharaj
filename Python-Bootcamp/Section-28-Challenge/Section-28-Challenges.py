# Challenge 1
import csv
people = [
['Dan', 34, 'Bucharest'],
['Andrei',21, 'London'],
['Maria', 45, 'Paris']
]

with open('people.csv', 'w') as f:
    writer = csv.writer(f)
    for i in people:
        writer.writerow(i)
with open('people.csv') as f:
    read = csv.reader(f)
    for r in read:
        print(r)
# =====================================================================================================================
# Challenge 2
# =====================================================================================================================
