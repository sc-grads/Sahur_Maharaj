import subprocess

with open('ip_addr.txt') as f:
    ip = f.read().splitlines()
    for i in ip:
        try:
            command = f'ping -n 1 {i}'
            output = subprocess.check_output(command.split())
            print(output.decode())
        except Exception as err:
            print(f'Host {i} is down')