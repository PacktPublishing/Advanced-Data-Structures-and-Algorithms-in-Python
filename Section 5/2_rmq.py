import numpy as np
from random import randint


def naive_query(array, a, b):
    return min(array[a:b+1])


def compute_rmq_table(array):
    n = len(array)
    log2n = int(np.log2(n))
    dp = np.zeros((log2n + 1, n))
    dp[0, :] = array
    pow = 1
    for i in range(1, log2n + 1):
        for j in range(n):
            dp[i, j] = dp[i - 1, j]
            if j + pow < n:
                dp[i, j] = min(dp[i, j], dp[i - 1, j + pow])
        pow *= 2
    return dp


def dp_query(array, a, b, dp):
    k = int(np.log2(b - a + 1))
    return min(dp[k, a], dp[k, b - 2**k + 1])


for tests in range(100):
    array = []
    n = randint(1, 1000)
    for i in range(n):
        array.append(randint(1, 1000))

    dp = compute_rmq_table(array)
    for _ in range(2000):
        a = randint(0, n - 1)
        b = randint(a, n - 1)
        with_naive = naive_query(array, a, b)
        with_dp = dp_query(array, a, b, dp)
        assert with_dp == with_naive, \
            'naive={}, efficient dp={},\nn={},\na={}\n={}\narray={}'.format(
                with_naive,
                with_dp,
                n,
                a,
                b,
                array
            )


