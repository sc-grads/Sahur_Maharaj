# Challenge 1
import csv
people = [
['Dan', 34, 'Bucharest'],
['Andrei',21, 'London'],
['Maria', 45, 'Paris']
]

with open('people.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for i in people:
        writer.writerow(i)
with open('people.csv') as f:
    read = csv.reader(f)
    for r in read:
        print(r)
# =====================================================================================================================
# Challenge 2
with open('people_new.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=':')
    for w in people:
        writer.writerow(w)
with open('people_new.csv') as f:
    read = csv.reader(f, delimiter=':')
    for r in read:
        print(r)
# =====================================================================================================================
