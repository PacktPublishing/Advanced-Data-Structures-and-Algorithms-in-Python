from collections import deque
from random import randint

def trivial(array, k):
    n = len(array)
    max_len = 0
    for i in range(n):
        for j in range(i, n):
            min_val = min(array[i:j+1])
            max_val = max(array[i:j+1])
            if max_val - min_val <= k:
                max_len = max(max_len, j - i + 1)
    return max_len

def length_ok(array, length, k):
    maximum = max(array[:length])
    minimum = min(array[:length])
    d_max = deque()
    d_min = deque()
    d_max.append(0)
    d_min.append(0)
    result = maximum - minimum <= k
    for i in range(len(array)):
        if i - d_min[0] == length:
            d_min.popleft()
        if i - d_max[0] == length:
            d_max.popleft()
        while len(d_min) and array[d_min[-1]] >= array[i]:
            d_min.pop()
        while len(d_max) and array[d_max[-1]] <= array[i]:
            d_max.pop()
        d_min.append(i)
        d_max.append(i)

        if i >= length:
            minimum = array[d_min[0]]
            maximum = array[d_max[0]]
            result = result or (maximum - minimum <= k)

    return result

def efficient(array, k):
    left = 1
    right = len(array)
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if length_ok(array, mid, k):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer


def optimal(array, k):
    d_max = deque()
    d_min = deque()
    d_max.append(0)
    d_min.append(0)
    max_len = 0
    start = 0
    for i in range(len(array)):
        while len(d_min) and array[d_min[-1]] >= array[i]:
            d_min.pop()
        while len(d_max) and array[d_max[-1]] <= array[i]:
            d_max.pop()
        d_min.append(i)
        d_max.append(i)
        while array[d_max[0]] - array[d_min[0]] > k:
            start += 1
            if len(d_min) and d_min[0] < start:
                d_min.popleft()
            if len(d_max) and d_max[0] < start:
                d_max.popleft()
        if len(d_max) and len(d_min):
            maximum = array[d_max[0]]
            minimum = array[d_min[0]]
            if maximum - minimum <= k:
                max_len = max(max_len, i - start + 1)
    return max_len

for tests in range(1000):
    array = []
    for i in range(randint(20, 100)):
        array.append(randint(1, 100))
    k = randint(40, 100)
    with_binary_search = efficient(array, k)
    trivial_result = trivial(array, k)
    optimal_result = optimal(array, k)
    assert with_binary_search == trivial_result, \
        'binary search={}, trivial={}, array={}, k={}'.format(
            with_binary_search,
            trivial_result,
            array,
            k
        )
    assert optimal_result == trivial_result, \
        'optimal={}, trivial={}, array={}, k={}'.format(
            optimal_result,
            trivial_result,
            array,
            k
        )








