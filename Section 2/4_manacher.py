import random


def naive(string):
    n = len(string)
    max_len = 0
    for i in range(n):
        for j in range(i, n):
            substr = string[i:j+1]
            if substr == substr[::-1]:
                max_len = max(max_len, j - i + 1)
    return max_len

def manacher(string):
    string = '~ ' + ' '.join(string) +' !'
    n = len(string)
    L = [0] * (n+1) # is n enough here?
    c = 0
    r = 1
    for i in range(2, n-1):
        i_mirror = 2*c - i
        if r > i:
            L[i] = min(L[i_mirror], r - i)
        while string[i + 1 + L[i]] == string[i - 1 - L[i]]:
            L[i] += 1
        if i + L[i] > r:
            c = i
            r = i + L[i]
    return max(L)

print(manacher('abcbabc'))
characters = 'abcde'
str = ''
for j in range(1000000):
    str += random.choice(characters)
print('Done generating')
print(manacher(str))
for i in range(1000):
    length = random.randint(1, 100)
    str = ''
    for j in range(length):
        str += random.choice(characters)

    naive_res = naive(str)
    manacher_res = manacher(str)
    assert naive_res == manacher_res, 'step={}, naive={}, ' \
                                       'manacher={}, string = {}'.format(
        i,
        naive_res,
        manacher_res,
        str
    )
