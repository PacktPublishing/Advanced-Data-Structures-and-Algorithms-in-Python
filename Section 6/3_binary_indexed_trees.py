from random import randint


def naive_query(array, a, b):
    return sum(array[a:b+1])


def naive_update(array, k, v):
    array[k] += v


def two_pow_trailing_zeros(x):
    return (x ^ (x - 1)) & x


def query(BIT, a, b):
    a += 1
    b += 1

    def inner(t):
        result = 0
        while t > 0:
            result += BIT[t]
            t -= two_pow_trailing_zeros(t)
        return result
    return inner(b) - inner(a - 1)


def update(BIT, k, v):
    k += 1
    n = len(BIT)
    while k < n:
        BIT[k] += v
        k += two_pow_trailing_zeros(k)


def build(array):
    BIT = [0] * (len(array) + 1)
    for i, v in enumerate(array):
        update(BIT, i, v)
    return BIT


for tests in range(100):
    array = []
    n = randint(1, 1000)
    for i in range(n):
        array.append(randint(1, 1000))

    BIT = build(array)
    for _ in range(2000):
        if randint(1, 2) % 2 == 0:
            # query
            a = randint(0, n - 1)
            b = randint(a, n - 1)
            with_naive = naive_query(array, a, b)
            with_BIT = query(BIT, a, b)
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
            k = randint(0, n - 1)
            v = randint(1, 1000)
            naive_update(array, k, v)
            update(BIT, k, v)
