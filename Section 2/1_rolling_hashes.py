import random

def naive(str):
    str_rev = str[::-1]
    n = len(str)
    for i in range(n, -1, -1):
        if str_rev[:i] == str_rev[i-1::-1]:
            return str + str_rev[i:]

def rolling_hashes(str):
    p = 23
    P = 666013
    str_rev = str[::-1]
    f_forward = 0
    f_backward = 0
    p_power = 1
    max_suffix_palindrome = 0
    for i, c in enumerate(str_rev):
        c_idx = ord(c) - ord('a')
        f_forward = (f_forward + c_idx*p_power) % P
        f_backward = (f_backward*p + c_idx) % P
        p_power *= p # p_power %= P?
        if f_forward == f_backward:
            max_suffix_palindrome = i
    return str + str_rev[max_suffix_palindrome+1:]


str = 'loaded'
print(naive(str))
print(rolling_hashes(str))

characters = 'abcdefghijklmnopq'
for i in range(10000):
    length = random.randint(1, 20)
    str = ''
    for j in range(length):
        str += random.choice(characters)

    naive_res = naive(str)
    hashes_res = rolling_hashes(str)
    assert naive_res == hashes_res, 'step={}, naive={}, hashes={}'.format(
        i,
        naive_res,
        hashes_res
    )






























