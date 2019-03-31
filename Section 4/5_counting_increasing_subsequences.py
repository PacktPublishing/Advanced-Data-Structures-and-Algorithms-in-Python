from random import randint

import numpy as np


def first_dp(array, k):
    n = len(array)
    dp = np.zeros((n, k))
    dp[:, 0] = 1
    for i in range(n):
        for p in range(i):
            if array[i] > array[p]:
                for j in range(1, k):
                    dp[i, j] += dp[p, j -1]
    return sum(dp[:, k - 1])


def second_dp(array, k):
    n = len(array)
    dp = np.zeros((n,k))
    dp[:, 0] = 1
    for j in range(1, k):
        num = {} # num[v] = how many subsequences of length j end with v
        for i in range(1, n):
            if array[i - 1] in num:
                num[array[i - 1]] += dp[i - 1, j - 1]
            else:
                num[array[i - 1]] = dp[i - 1, j - 1]

            for p in range(array[i]):
                if p in num:
                    dp[i, j] += num[p]
    return sum(dp[:, k - 1])


for tests in range(1000):
    array = []
    for i in range(randint(20, 100)):
        array.append(randint(1, 100))
    k = randint(5, 20)
    with_first = first_dp(array, k)
    with_second = second_dp(array, k)
    assert with_first == with_second, \
        'first={}, second={},\narray={},\nk={}'.format(
            with_first,
            with_second,
            array,
            k
        )


