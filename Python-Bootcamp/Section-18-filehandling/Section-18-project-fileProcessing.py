with open('ignoretxtfiles/devices.txt') as f:
    con = f.read().splitlines()
    device = list()
    for line in con[1:]:
        device.append(line.split(':'))

    print(device)
    for d in device:
        print(f'Ip is: {d[1]}')
