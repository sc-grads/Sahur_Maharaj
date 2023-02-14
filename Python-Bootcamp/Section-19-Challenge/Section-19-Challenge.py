import time

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
# Challenge 4
def tail(file, e):
    with open(file) as f:
        content = f.read().splitlines()
        end = content[len(content) - e:]
        content_str = f'\n{end}'
        return content_str


print(tail('txtfiles/sample_filec4.txt', 5))
# =====================================================================================================================
# Challenge 5
while True:
    t = tail('txtfiles/sample_filec4.txt', 3)
    print(t)
    time.sleep(3)
    print('')
    break


# =====================================================================================================================
# Challenge 6
def count_file(file):
    with open(file) as f:
        content = f.read().splitlines()
        lines = len(content)
        words = 0
        for line in content:
            words += len(line.split(' '))
        chars = 0
        for c in content:
            c += len(list(c))
        return lines, words, c


print(count_file('txtfiles/sample_filec4.txt'))
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
