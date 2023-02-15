with open('show_arp.txt') as f:
    content = f.read().splitlines()
    content = content[1:]
    ip_mac = list()
    for l in content:
        ip = l.split()[1]
        mac = l.split()[3]

        ip_mac.append((ip, mac))

    print(ip_mac)