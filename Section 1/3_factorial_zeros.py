def zeros(n):
    num_zeros = 0
    while n:
        num_zeros += n // 5
        n //= 5

    return num_zeros

def linear_search(num_zeros):
    n = 0
    while zeros(n) < num_zeros:
        n += 1

    if zeros(n) == num_zeros:
        return n
    return None

def binary_search(num_zeros):

    left = 0
    right = 5*num_zeros
    while left < right:
        middle = (left + right) // 2
        if zeros(middle) < num_zeros:
            left = middle + 1
        else:
            right = middle

    if zeros(left) == num_zeros:
        return left
    return None


for i in range(101):
    print(i, binary_search(i))
    assert binary_search(i) == linear_search(i)









