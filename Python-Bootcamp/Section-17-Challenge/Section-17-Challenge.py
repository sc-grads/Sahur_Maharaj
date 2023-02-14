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


# find_large_prime()  # Takes extremely long to complete
# print(large_prime)  # Takes extremely long to complete


# =====================================================================================================================
# Challenge 6
def fibo(fib_to):
    a, b = 0, 1
    while a <= fib_to:
        print(a, ' ', end=' ')
        a, b = b, a + b


print(fibo(100))


# =====================================================================================================================
# Challenge 7
def equi_ind(ind):
    for i in range(0, len(ind)):
        if sum(ind[:i]) == sum(ind[i + 1:]):
            return i
    return False


find_ind = [-7, 1, 5, 2, -4, 3, 0]
print(equi_ind(find_ind))
# =====================================================================================================================
# Challenge 8
def eqi_indx(commastr):
    numbs = commastr.split(',')
    numbs_lst = [int(num) for num in numbs]

    for i in range(0, len(numbs_lst)):
        if sum(numbs_lst[:i]) == sum(numbs_lst[i + 1:]):
            return i
    return False
print(eqi_indx('-7,1,5,2,-4,3,0'))
# =====================================================================================================================
# Challenge 9

# =====================================================================================================================
