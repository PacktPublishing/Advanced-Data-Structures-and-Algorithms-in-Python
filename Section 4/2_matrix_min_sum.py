import numpy as np


def run_recursive(array):
    def inner(line, col):
        if line < 0 or col < 0:
            return 10**20
        if line == 0 and col == 0:
            return array[line, col]
        return array[line, col] + min(inner(line - 1, col),
                                      inner(line, col - 1))

    n = array.shape[0]
    return inner(n - 1, n - 1)


def print_path(dp, array, line, col):
    prev_dp = dp[line, col] - array[line, col]
    if col - 1 >= 0 and prev_dp == dp[line, col - 1]:
        print_path(dp, array, line, col - 1)
    elif line - 1 >= 0 and prev_dp == dp[line - 1, col]:
        print_path(dp, array, line - 1, col)
    print(line, col)


def run_dp(array):
    dp = np.zeros_like(array)
    n = dp.shape[0]
    dp[0, 0] = array[0, 0]
    for i in range(1, n):
        dp[0, i] = dp[0, i - 1] + array[0, i]
        dp[i, 0] = dp[i - 1, 0] + array[i, 0]
    for i in range(1, n):
        for j in range(1, n):
            dp[i, j] = array[i, j] + min(dp[i - 1, j], dp[i, j - 1])
    print_path(dp, array, n - 1, n - 1)
    return dp[n - 1, n - 1]


def run_dp_memory_optimized(array):
    dp1 = np.zeros_like(array[0])
    dp2 = np.zeros_like(array[0])
    n = dp1.shape[0]
    dp1[0] = array[0, 0]
    for i in range(1, n):
        dp1[i] = dp1[i - 1] + array[0, i]
    for i in range(1, n):
        dp2[0] = dp1[0] + array[i, 0]
        for j in range(1, n):
            dp2[j] = array[i, j] + min(dp1[j], dp2[j - 1])
        dp1[:] = dp2
    return dp1[n - 1]


array = np.array([
    [4, 3, 4, 31],
    [1, 15, 9, 11],
    [71, 13, 10, 6],
    [21, 41, 51, 2]
])

print('Recursive:', run_recursive(array))
print('DP:', run_dp(array))
print('Memory optimized DP:', run_dp_memory_optimized(array))
























