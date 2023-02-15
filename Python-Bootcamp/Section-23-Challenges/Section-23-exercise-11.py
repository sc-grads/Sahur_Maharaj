my_str  = 'wlo1      Link encap:Ethernet  HWaddr b4:6d:83:77:85:f3'

# YOUR CODE STARTS HERE
intr_lst = my_str.split()
interface_mac = intr_lst[0] + '!' + intr_lst[-1]
print(interface_mac)