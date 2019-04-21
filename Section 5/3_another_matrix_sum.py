import numpy as np

MOD = 666013


def run_classic_dp(n, m):
    dp = np.zeros((m+1, n, n))
    dp[0, 0, 0] = 1
    for k in range(1, m+1):
        for i in range(n):
            for j in range(n):
                n1 = dp[k-1, i-1, j] if i-1 >= 0 else 0
                n2 = dp[k-1, i, j-1] if j-1 >= 0 else 0
                n3 = dp[k-1, i+1, j] if i+1 < n else 0
                n4 = dp[k-1, i, j+1] if j+1 < n else 0
                dp[k, i, j] = n1 + n2 + n3 + n4
                dp[k, i, j] %= MOD
    return dp[m, n-1, n-1]


def run_new_dp(n, m):
    log2m = int(np.log2(m))
    dp = np.zeros((log2m+1, n, n, n, n))
    for i in range(n):
        for j in range(n):
            if i + 1 < n:
                dp[0, i, j, i + 1, j] = 1
            if i - 1 >= 0:
                dp[0, i, j, i - 1, j] = 1
            if j + 1 < n:
                dp[0, i, j, i, j + 1] = 1
            if j - 1 >= 0:
                dp[0, i, j, i, j - 1] = 1

    for k in range(1, log2m + 1):
        for i1 in range(n):
            for j1 in range(n):
                for i2 in range(n):
                    for j2 in range(n):
                        for p in range(n):
                            for q in range(n):
                                dp[k, i1, j1, i2, j2] += dp[k-1, i1, j1, p, q] *\
                                                         dp[k-1, p, q, i2, j2]
                                dp[k, i1, j1, i2, j2] %= MOD

    if 2 ** log2m == m:
        return dp[log2m, 0, 0, n - 1, n - 1]
    binary = '{0:b}'.format(m)[::-1]
    results = None
    for i, b in enumerate(binary):
        if b == '1' and results is None:
            results = dp[i, 0, 0, :, :]
        elif b == '1':
            new_results = np.zeros_like(results)
            for k1 in range(n):
                for k2 in range(n):
                    for p in range(n):
                        for q in range(n):
                            new_results[k1, k2] += results[p, q] *\
                                                   dp[i, p, q, k1, k2]
                            new_results[k1, k2] %= MOD
            results = new_results
    return results[n - 1, n - 1]

print(run_classic_dp(6, 100))
print(run_new_dp(6, 100))
print(run_new_dp(5, 10 ** 18))

for n in range(2, 5):
    for m in range(2, 100):
        classic = run_classic_dp(n, m)
        new = run_new_dp(n, m)
        assert classic == new, 'classic={}, new={}, n={}, m={}'.format(
            classic,
            new,
            n,
            m
        )


