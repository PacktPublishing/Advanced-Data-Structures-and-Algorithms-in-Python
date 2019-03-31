import numpy as np

inf = 10 ** 20


def run_recursive(array, m):
    n = array.shape[0]

    def inner(k, line, col):
        if k < 0 or line < 0 or col < 0 or line >= n or col >= n:
            return inf
        if k == 0 and line == 0 and col == 0:
            return array[line, col]

        return array[line, col] + min(inner(k - 1, line - 1, col),
                                      inner(k - 1, line, col - 1),
                                      inner(k - 1, line + 1, col),
                                      inner(k - 1, line, col + 1))
    return inner(m, n - 1, n - 1)


def run_dp(array, m):
    n = array.shape[0]
    dp = np.ones((m+1, n, n)) * inf
    dp[0, 0, 0] = array[0, 0]
    for k in range(1, m+1):
        for i in range(n):
            for j in range(n):
                n1 = dp[k-1, i-1, j] if i-1 >= 0 else inf
                n2 = dp[k-1, i, j-1] if j-1 >= 0 else inf
                n3 = dp[k-1, i+1, j] if i+1 < n else inf
                n4 = dp[k-1, i, j+1] if j+1 < n else inf
                dp[k, i, j] = array[i, j] + min(n1, n2, n3, n4)
    return dp[m, n-1, n-1]


array = np.array([
    [4, 3, 4, 31],
    [1, 15, 9, 11],
    [71, 13, 10, 6],
    [21, 41, 51, 2]
])

print(run_recursive(array, 10))
print(run_dp(array, 10))