import csv
with open('airtravel.csv') as f:
    reader = csv.reader(f)
    next(reader)
    year_1958 = dict()
    for r in reader:
        # print(r)
        year_1958[r[0]] = r[1]
        max_1959 = max(year_1958.values())
        print(max_1959)
        for k, v in year_1958.items():
            if max_1959 == v:
                print(f'Month: {k}, Flights: {v.strip()}')

