from random import randint
import numpy as np

MOD = 666013

def naive(n, d):

    def inner(number):
        if len(number) == n:
            digital_sum = sum(int(digit) for digit in number)
            count = 0
            if digital_sum % d == 0:
                count += 1
            return count
        count = 0
        for digit in range(10):
            count += inner(number + str(digit))
        return count

    return inner('')


def dp_naive(n, d):
    dp = np.zeros((n, d))
    for i in range(10):
        dp[0, i % d] += 1  # 0 = 1 digit numbers

    for i in range(1, n):
        for j in range(d):
            for k in range(10):
                dp[i, j] += dp[i - 1, (j - k) % d]
            dp[i, j] %= MOD

    return dp[n - 1, 0]


def dp_efficient(n, d):
    log2n = int(np.log2(n))
    dp = np.zeros((log2n + 1, d))
    for i in range(10):
        dp[0, i % d] += 1
    for i in range(1, log2n + 1):
        for k1 in range(d):
            for k2 in range(d):
                h = (k1 + k2) % d
                dp[i, h] += dp[i - 1, k1] * dp[i - 1, k2]
                dp[i, h] %= MOD

    if 2 ** log2n == n:
        return dp[log2n, 0]
    binary = '{0:b}'.format(n)[::-1]
    results = None
    for i, b in enumerate(binary):
        if b == '1' and results is None:
            results = dp[i, :]
        elif b == '1':
            new_results = np.zeros_like(results)
            for k1 in range(d):
                for k2 in range(d):
                    h = (k1 + k2) % d
                    new_results[h] += dp[i, k1] * results[k2]
                    new_results[h] %= MOD
            results = new_results
    return results[0]


print(naive(6, 3))
print(dp_naive(6, 3))
print(dp_efficient(6, 3))
print(dp_efficient(10 ** 18, 100))

for tests in range(100):
    array = []
    n = randint(1, 1000)
    d = randint(1, 100)
    with_naive_dp = dp_naive(n, d)
    with_efficient_dp = dp_efficient(n, d)
    assert with_naive_dp == with_efficient_dp, \
        'naive dp={}, efficient dp={},\nn={},\nd={}'.format(
            with_naive_dp,
            with_efficient_dp,
            n,
            d
        )

