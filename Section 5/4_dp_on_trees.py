import numpy as np


def count_bsts(n):
    dp = np.zeros(n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]
    return dp[n]


print(count_bsts(1))
print(count_bsts(2))
print(count_bsts(3))
print(count_bsts(4))
print(count_bsts(5))
print(count_bsts(6))
print(count_bsts(7))
print(count_bsts(9))
print(count_bsts(10))


















