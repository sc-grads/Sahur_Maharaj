import csv

with open('people.csv', 'a') as f:
    writer = csv.writer(f)
    csv_data = (5, 'Anne', 'Amsterdam')
    writer.writerow(csv_data)


with open('numbers.csv', 'w', newline='') as f:
    writer_n = csv.writer(f)
    writer_n.writerow(['x', 'x * 2', 'x * 3', 'x * x'])
    for x in range(1, 101):
        writer_n.writerow([x, x * 2, x * 3, x * x])
