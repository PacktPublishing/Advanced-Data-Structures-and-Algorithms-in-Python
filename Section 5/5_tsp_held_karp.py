import numpy as np

inf = 10 ** 18


def generate_d(n):
    d = np.zeros((n, n), dtype=np.int64)
    for i in range(n):
        for j in range(i+1, n):
            d[i, j] = np.random.randint(1, 10)
            if d[i, j] == 0:
                d[i, j] = inf
            d[j, i] = d[i, j]
    return d


def brute_force(n, d):

    def inner(current_node, current_length, visited=set()):
        if len(visited) == n - 1:
            return current_length + d[current_node, 0]

        best = inf
        for i in range(1, n):
            if i not in visited:
                best = min(best, inner(i,
                                       current_length + d[current_node, i],
                                       visited | {i}))
        return best

    return inner(0, 0)


def run_dp(n, d):
    dp = np.ones((2 ** n, n)) * inf
    # dp[S, c] = sum of the minimum sum tour that visits all cities
    #            corresponding to the indexes of the set bits in S [...]
    # S = 10011 => 0, 1, 4
    for c in range(1, n):
        dp[1 << c, c] = d[0, c] # 1 << 3 => 1000

    for S in range(2**n - 1): # 111...1110
        for c in range(1, n):
            if S & (1 << c) != 0:
                S_no_c = S - (1 << c)
                for c1 in range(1, n):
                    if S & (1 << c1) != 0:
                        dp[S, c] = min(dp[S, c], dp[S_no_c, c1] + d[c1, c])

    final_state = 2**n - 2
    best = inf
    for c in range(1, n):
        best = min(best, dp[final_state, c] + d[c, 0])
    return best



for i in range(10):
    n = np.random.randint(2, 5)
    d = generate_d(n)

    print(d)
    print('brute force search :', brute_force(n, d))
    print('dynamic programming:', run_dp(n, d))
    print('-' * 20)
