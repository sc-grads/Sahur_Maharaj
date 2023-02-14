import time
import string
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
            chars += len(list(c))
        return lines, words, c
print(count_file('txtfiles/sample_filec4.txt'))
# =====================================================================================================================
# Challenge 7
with open('txtfiles/banking.txt') as f:
    content = f.read().splitlines()
    deposit, withdrawal = 0, 0
    for item in content:
        tmp = item.split(':')
        if tmp[0] == 'D':
            deposit += int(tmp[1])
        elif tmp[0] == 'W':
            withdrawal += int(tmp[1])
        else:
            print('File format error')
    balance = deposit - withdrawal
    print(balance)
# =====================================================================================================================
# Challenge 8
with open('txtfiles/f1.txt', 'a') as f:
    f.write('well hello')
    file1 = f.read().splitlines()

with open('txtfiles/f2.txt', 'a') as f:
    f.write('hello python')
    file2 = f.read().splitlines()
file = list(zip(file1, file2))

i = 0
for item in file:
    i += 1
    if item[0] != item[1]:
        print(f'file1 ({i}): {item[0]}, file2 ({i}): {item[1]}')
# =====================================================================================================================
# Challenge 9
with open('txtfiles/american-english.txt') as f:
    words = f.read().splitlines()
    words_and_length = dict()
    for w in words:
        words_and_length[w] = len(w)
    for k, v in words_and_length.items():
        print(f'{k} -> {v}')
# =====================================================================================================================
# Challenge 10
with open('txtfiles/american-english.txt') as f:
    words = f.read().splitlines()
    words_and_length = dict()
    for w in words:
        words_and_length[w] = len(w)
    words_list = sorted(words_and_length.items(), key=lambda x:x[1], reverse=True)
    print(words_list[:100])
# =====================================================================================================================
# Challenge 11
letters = dict()
for c in string.ascii_letters:
    letters[c] = 0

with open('txtfiles/american-english.txt') as words:
    for w in words:
        for char in string.ascii_letters:
            letters[char] += w.count(char)

print(letters)
# =====================================================================================================================
# Challenge 12
letters = dict()
for c in string.ascii_letters:
    letters[c] = 0

with open('txtfiles/american-english.txt') as words:
    for w in words:
        for char in string.ascii_letters:
            letters[char] += w.lower().count(char)

print(letters)
# =====================================================================================================================
# Challenge 13
letters = dict()
for c in string.ascii_letters:
    letters[c] = 0

with open('txtfiles/american-english.txt') as words:
    for w in words:
        for char in string.ascii_letters:
            letters[char] += w.count(char)

print(sorted(letters.items(), key=lambda x:x[1], reverse=True))
# =====================================================================================================================
