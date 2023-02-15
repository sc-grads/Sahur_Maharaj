import os
out = os.popen('arp -a').read()
print(out)

os.system('type nul > abc.txt')