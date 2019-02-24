from collections import deque
from random import randint

def trivial(array, length):
    maximum = min(array[:length])
    for i in range(len(array)-length+1):
        minimum = min(array[i:i+length])
        maximum = max(maximum, minimum)

    return maximum

def with_deque(array, length):
    maximum = min(array[:length])
    d = deque()
    d.append(0)
    for i in range(len(array)):
        if i - d[0] == length:
            d.popleft()
        while len(d) and array[d[-1]] >= array[i]:
            d.pop()
        d.append(i)
        if i >= length:
            maximum = max(maximum, array[d[0]])

    return maximum

for tests in range(10000):
    array = []
    for i in range(20):
        array.append(randint(1,100))
    length = randint(1,10)
    with_deque_result = with_deque(array, length)
    trivial_result = trivial(array, length)
    assert with_deque_result == trivial_result, \
        'deque={}, trivial={}, array={}, length={}'.format(
            with_deque_result,
            trivial_result,
            array,
            length
        )








