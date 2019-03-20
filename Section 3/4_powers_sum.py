import numpy as np

def naive(A, n):
    result = np.zeros_like(A)
    power = A
    for i in range(1, n+1):
        result += power
        power = np.matmul(power, A) % 666013
        result %= 666013
    return result

def optimal(A, n):
    # n = 2k    => S = (I+A^k)(A+...+A^k)
    # n = 2k+1  => S = (I+A^k)(A+...+A^k)+A^(2k+1)
    # n = 1 =>  => S = A
    eye = np.eye(A.shape[0])
    def inner(A, n):
        if n == 1:
            return A, A

        A_pow_n_div2, S_n_div2 = inner(A, n // 2)
        A_pow_n = np.matmul(A_pow_n_div2, A_pow_n_div2) % 666013
        S_n = np.matmul(eye + A_pow_n_div2, S_n_div2)
        if n % 2 == 0:
            return A_pow_n % 666013, S_n % 666013
        A_pow_n = np.matmul(A_pow_n, A) % 666013
        return A_pow_n % 666013, (S_n + A_pow_n) % 666013
    return inner(A, n)[1]



n = 1000
arr = np.array([[1,2],[3,4]], dtype=np.int64)
print(naive(arr, n))
print(optimal(arr, n))

for i in range(1, 1000):
    assert np.array_equal(naive(arr, i), optimal(arr, i))
