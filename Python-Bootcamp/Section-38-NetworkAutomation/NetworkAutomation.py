# # encodeing and decodeing
# s1 = 'abc'
# b1 = s1.encode('utf-8')
#
# print(type(b1))
# print(b1[0])
# print(b1[1])
# print(b1)
#
# s2 = 'gwsrger'
# b2 = s2.encode()
# print(b2)
# print(b2[0])
#
#
#
# import telnetlib
# import time
#
# host = '10.1.1.10'
# port = '23'
# user = 'u1'
# password = 'cisco'
#
# tn = telnetlib.Telnet(host=host, port=port)
# tn.read_until(b'Username: ')
# tn.write(user.encode() + b'\n')
# tn.read_until(b'Password: ')
# tn.write(password.encode() + b'\n')
#
# tn.write(b'show ip interface brief\n')
# tn.write(b'exit\n')
# time.sleep(1)
#
# out = tn.read_all()
# print(out.decode())
import time

import paramiko

ssh_client = paramiko.SSHClient()
# ssh_client.connect(hostname='10.0.0.1', port=22,
#                 username='u1', password='cisco', look_for_keys=False, allow_agent=False)

router = {'hostname': '10.1.1.10', 'port': '22', 'username': 'u1', 'password': 'cisco'}
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
print(ssh_client.get_transport().is_active())
shell = ssh_client.invoke_shell()
shell.send(b'terminal length 0\n')
shell.send(b'show version\n')
shell.send(b'show ip int brief\n')
time.sleep(2)
out = shell.recv(10000)
print(out.decode())

if ssh_client.get_transport().is_active():
    ssh_client.close()
