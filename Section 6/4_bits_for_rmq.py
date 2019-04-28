from random import randint

inf = 10 ** 20


def naive_query(array, a, b):
    return min(array[a:b+1])


def naive_update(array, k, v):
    array[k] += v


def two_pow_trailing_zeros(x):
    return (x ^ (x - 1)) & x


def query(array, BIT, a, b):
    result = 0
    while a <= b:
        to_sub = two_pow_trailing_zeros(b)
        if b - to_sub + 1 >= a:
            if array[ BIT[b] ] < array[result]:
                result = BIT[b]
            b -= to_sub
        else:
            if array[b] < array[result]:
                result = b
            b -= 1
    return result


def update(array, BIT, k, v):
    array[k] += v
    n = len(array) - 1
    init_k = k
    while k <= n:
        if BIT[k] == init_k:
            to_sub = two_pow_trailing_zeros(k)
            q = query(array, BIT, k - to_sub + 1, k - 1)
            if array[q] < array[k]:
                BIT[k] = q
            else:
                BIT[k] = k
        else:
            if array[init_k] < array[ BIT[k] ]:
                BIT[k] = init_k
        k += two_pow_trailing_zeros(k)


def build(array):
    BIT = [0] * (len(array) + 1)
    for i, v in enumerate(array[1:]):
        update(array, BIT, i + 1, v)
    return BIT


for tests in range(100):

    array = [inf]
    n = randint(1, 1000)
    for i in range(n):
        array.append(randint(1, 1000))

    BIT = build(array)
    for _ in range(2000):
        if randint(1, 2) % 2 == 0:
            # query
            a = randint(1, n)
            b = randint(a, n)
            with_naive = naive_query(array, a, b)
            with_BIT = array[query(array, BIT, a, b)]
            assert with_BIT == with_naive, \
                'naive={}, efficient={},\nn={},\na={}\nb={}\narray={}'.format(
                    with_naive,
                    with_BIT,
                    n,
                    a,
                    b,
                    array
                )
        else:
            k = randint(1, n)
            v = randint(-1000, 1000)
            naive_update(array, k, v)
            update(array, BIT, k, v)
