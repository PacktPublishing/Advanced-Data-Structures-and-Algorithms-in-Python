from random import randint

def in_n_cubed(array, k):
    n = len(array)
    min_len = n + 1
    for i in range(n):
        for j in range(i, n):
            if sum(array[i:j+1]) % k == 0 and j - i + 1 < min_len:
                min_len = j - i + 1

    return min_len

def efficient(array, k):
    n = len(array)
    min_len = n + 1
    last_prefix_idx = {0: -1}
    current_sum = 0
    for i in range(n):
        current_sum = (current_sum + array[i]) % k
        if current_sum in last_prefix_idx:
            length = i - last_prefix_idx[current_sum]
            if length < min_len:
                min_len = length
        last_prefix_idx[current_sum] = i

    return min_len
for tests in range(100):
    array = []
    for i in range(200):
        array.append(randint(1, 100))
    k = randint(1, 10)
    n_cubed_result = in_n_cubed(array, k)
    efficient_result = efficient(array, k)
    assert n_cubed_result == efficient_result, \
        'n_cubed={}, efficient={}, array={}, k={}'.format(
            n_cubed_result,
            efficient_result,
            array,
            k
        )
