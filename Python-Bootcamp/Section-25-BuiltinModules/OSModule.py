import os, subprocess

out = os.popen('arp -a').read()
print(out)

# os.system('type nul > abc.txt')  <-- creates a file

cmd = ['arp', '-a']
subprocess.check_output(cmd)
cmd_ping = ['ping', '-n', '300', '8.8.8.8']
outpt = subprocess.check_output(cmd_ping)
print(str(outpt.decode()))

