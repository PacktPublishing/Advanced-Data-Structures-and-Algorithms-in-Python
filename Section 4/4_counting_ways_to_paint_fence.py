import numpy as np


def dp_2_states(n, k):
    dp = np.zeros((n, k))
    dp[0, :] = 1
    dp[1, :] = k
    for i in range(2, n):
        for c in range(k):
            s = 0
            for c1 in range(k):
                if c1 != c:
                    s += dp[i - 2, c1] + dp[i - 1, c1]
            dp[i, c] = s
    return sum(dp[n - 1, :])


def dp_1_state(n, k):
    dp = np.zeros(n)
    dp[0] = k
    dp[1] = k*k
    for i in range(2, n):
        dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2])
    return dp[n - 1]

n = 15
k = 6
print(dp_2_states(n, k))
print(dp_1_state(n, k))

