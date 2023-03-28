# Challenge 1
my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
mac_addr = my_str.split()[-1]   # <-- or: (my_str[-1:-18:-1]; mac = mac[::-1]) or: (my_str[len(my_str)-17:])
print(mac_addr)
# ======================================================================================================================
# Challenge 2
print('It displayed: "You\'ve got an error!" \\n means a new line. \\ is known as the escape character.')
# ======================================================================================================================
# Challenge 3
FOOT = 30.40  # ft --> cm
usr_val = float(input('Enter a value in feet: '))
print(f'The value of {usr_val}ft in CM is: {round(usr_val * FOOT, 2)}')
# ======================================================================================================================
# Challenge 4
word = input('Enter word to verify if it is a palindrome: ')
print(f'Is {word} a palindrome? --> {word == word[::-1]}')
# ======================================================================================================================
# Challenge 5
word.replace(' ', '')
word.lower()
print(f'Is {word} a palindrome? --> {word == word[::-1]}')
# ======================================================================================================================
# Challenge 6
my_word = input('Enter a string(min 2 chars): ')
new_word = my_word[:2] + my_word[-2:]
print(new_word)
# ======================================================================================================================
# Challenge 7
new_str = input('Enter a word: ')
elem_char = new_str[0]
revised_str = new_str[1:].replace(elem_char, '$')
revised_str = elem_char + revised_str
print(revised_str)
# ======================================================================================================================
# Challenge 8
indx = int(input('Enter an index to remove: '))
remove_str = input('Enter string to modify: ')
first_ind = remove_str[0:indx]
end_ind = remove_str[indx+1:]
print(first_ind + end_ind)
# ======================================================================================================================
# Challenge 9
chnge_str = input('What do you want to change: ')
print(chnge_str[::2])
# ======================================================================================================================
# Challenge 10
circ_radii = float(input('Enter Radius: '))
circ_area = 3.1415 * circ_radii ** 2
print(f'The radius of the circle is: {circ_radii}\nand the area is: {circ_area:.4f}')
# ======================================================================================================================
# Challenge 11
locte_sub_str = 'Hello hEllo hello HELLO june June Red Rose Green Rose Hello'
to_locate = 'hello'
locte_sub_str = locte_sub_str.lower()
num_occ = locte_sub_str.count(to_locate.lower())
print(f'{to_locate} is found {num_occ} in the current string')
# ======================================================================================================================
# Challenge 12
numb = 1234567
add_sep = f'{numb:,}'
print(add_sep.replace(',', '.'))

