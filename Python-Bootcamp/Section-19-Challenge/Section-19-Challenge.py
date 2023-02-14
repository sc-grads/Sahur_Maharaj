# Challenge 1
with open('txtfiles/macs.txt') as f:
    content = f.read().split()
    content = list(set(content))
with open('txtfiles/unique_macs.txt', 'a') as f:
    for mac_addr in content:
        f.write(f'{mac_addr}\n')
# =====================================================================================================================
# Challenge 2
with open('txtfiles/sample_file.txt') as f:
    content = f.read().splitlines()
    content_str = f'\n{content}'
    print(content_str)
# =====================================================================================================================
# Challenge 3
with open('txtfiles/file.txt') as f:
    content_lst = f.readlines()
remove_space = [l for l in content_lst if l.strip() != '']
with open('txtfiles/no_blanks.txt', 'a') as f:
    f.write(''.join(remove_space))
# =====================================================================================================================
# Challenge 1
# =====================================================================================================================
# Challenge 1
# =====================================================================================================================
# Challenge 1
# =====================================================================================================================
# Challenge 1
# =====================================================================================================================
# Challenge 1
# =====================================================================================================================
# Challenge 1
# =====================================================================================================================
# Challenge 1
# =====================================================================================================================
# Challenge 1
# =====================================================================================================================
# Challenge 1
# =====================================================================================================================
# Challenge 1
# =====================================================================================================================
