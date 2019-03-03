from random import randint

def naive(array, s):
    n = len(array)
    count = 0
    for i in range(n):
        for j in range(i, n):
            if sum(array[i:j+1]) == s:
                count += 1
    return count

def efficient(array, s):
    n = len(array)
    count = 0
    prefix_sum_counts = {0: 1}
    current_sum = 0
    '''
    current_sum[i] - current_sum[k-1] == s
    => array[k] + ... + array[i] == s
    => count how many are equal to current_sum[i] - s
       at each step
    '''
    for i in range(n):
        current_sum += array[i]
        if current_sum - s in prefix_sum_counts:
            count += prefix_sum_counts[current_sum - s]
        if current_sum in prefix_sum_counts:
            prefix_sum_counts[current_sum] += 1
        else:
            prefix_sum_counts[current_sum] = 1
    return count


for tests in range(100):
    array = []
    for i in range(200):
        array.append(randint(1, 100))
    s = randint(1, 10)
    naive_result = naive(array, s)
    efficient_result = efficient(array, s)
    assert naive_result== efficient_result, \
        'naive_res={}, efficient_res={}, array={}, s={}'.format(
            naive_result,
            efficient_result,
            array,
            s
        )




























