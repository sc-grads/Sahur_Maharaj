# Challenge 1
def uni_lst(lst):
    ord_lst = []
    for i in lst:
        if i not in ord_lst:
            ord_lst.append(i)
    return ord_lst


print(uni_lst([1, 2, 3, 3, 3, 3, 4, 5, 1, 3, 5, 5, 5]))


# =====================================================================================================================
# Challenge 2
def perfect_no(numb):
    div = []
    for i in range(1, int(numb / 2) + 1):
        if numb % i == 0:
            div.append(i)
    if sum(div) == numb:
        return f'{numb} is a perfect number'
    else:
        return f'{numb} is not a perfect number'


print(perfect_no(496))


# =====================================================================================================================
# Challenge 3
def fact(num):
    if num == 0:
        return 'Number can not be a factorial'
    else:
        end_f = 1
        while num > 0:
            end_f *= num
            num -= 1
        return f'Factorials are {end_f}'


print(fact(4))


# =====================================================================================================================
# Challenge 4
def prime_no(numbers):
    is_prime = True
    itr = 1
    while itr < numbers // 2:
        itr += 1
        if numbers % itr == 0:
            is_prime = False
            break
        else:
            is_prime = False
    return is_prime


print(prime_no(2))

# =====================================================================================================================
# Challenge 5
large_prime = []


def find_large_prime():
    for i in range(1_000_000, 100_000_000):
        if prime_no(i):
            large_prime.append()


find_large_prime()
print(large_prime)
# =====================================================================================================================
# Challenge 1

# =====================================================================================================================
# Challenge 1

# =====================================================================================================================
# Challenge 1

# =====================================================================================================================
# Challenge 1

# =====================================================================================================================
