# Challenge 1
c1_list = ['e', 'e', 2, 4, 'hello', 'hello']
print(f'Current list: {c1_list}')
while 'e' in c1_list:
    c1_list.remove('e')
print(f'Removed elements from list: {c1_list}')
# =====================================================================================================================
# Challenge 2
c2_list = [1, 1, 1, 1, 12, 23, 3, 3, 4, 4, 45, 434, 2, 2, 34, 6, 7, 423, 325, 6]
new_c2_list = []
for i in c2_list:
    if i not in new_c2_list:
        new_c2_list.append(i)
print(f'Old list: {c2_list}\nNew List removed duplicates: {new_c2_list}')
# =====================================================================================================================
# Challenge 3
nums = '10,20,30,40,50'
nums_list = nums.split(',')
num_list = [int(n) for n in nums_list]
print(num_list)
# =====================================================================================================================
# Challenge 4
c4_list = []
divis_mulit = [n for n in range(1500, 3201) if n % 7 == 0 and n % 5 != 0]
print(divis_mulit)
# =====================================================================================================================
# Challenge 5
c5_usr_str = input('Enter a Really Long String: ')
c5_list = c5_usr_str.split(' ')
c5_reverse = ' '.join(reversed(c5_list))
print(f'The string you typed out is: {c5_usr_str}\nconverted to a list is: {c5_list}\nthe reversed is :{c5_reverse}')
# =====================================================================================================================
# Challenge 6
c6_usr_str = input('Enter hyphenated values:> ')
c6_lst = c6_usr_str.split('-')
c6_lst.sort()
print(c6_lst)
# =====================================================================================================================
# Challenge 7
c7_usr_str = input('Enter Separated by Spaces: ')
c7_lst = c7_usr_str.split(' ')
c7_rev_lst = []
for w in c7_lst:
    c7_rev_lst.append(w[::-1])
print(c7_rev_lst)
# =====================================================================================================================
# Challenge 8
c8_usr_str = input('Enter Separated by Spaces -8: ')
c8_lst = c8_usr_str.split(' ')
c8_rev_lst = [rev[::-1] for rev in c8_lst]
print(c8_rev_lst)
# =====================================================================================================================
# Challenge 9
c9_lst = list('mamma mia mm')
place_h_lst = []
for i in set(c9_lst):
    total = c9_lst.count(i)
    place_h_lst.append((i, total))
print(place_h_lst)
# =====================================================================================================================
# Challenge 10
c10_lst = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
len_w_c10 = [(w, len(w)) for w in c10_lst]
print(len_w_c10)
# =====================================================================================================================

