from random import randint

import numpy as np

inf = 10 ** 20


def naive_query(array, a, b):
    return min(array[a:b+1])


def naive_update(array, k, v):
    array[k] = v


def query(n, segment_tree, a, b):
    def inner(node, left, right):
        if right < a or left > b:
            return inf
        if a <= left and right <= b:
            return segment_tree[node]
        m = (left + right) // 2
        return min(inner(2*node + 1, left, m),
                   inner(2*node + 2, m + 1, right))
    return inner(0, 0, n - 1)


def update(n, segment_tree, k, v):
    def inner(node, left, right):
        if k < left or k > right:
            return
        if left == right:
            segment_tree[node] = v
            return
        m = (left + right) // 2
        inner(2*node + 1, left, m)
        inner(2*node + 2, m + 1, right)
        segment_tree[node] = min(segment_tree[2*node + 1],
                                 segment_tree[2*node + 2])
    inner(0, 0, n - 1)

for tests in range(100):
    array = []
    n = randint(1, 1000)
    for i in range(n):
        array.append(randint(1, 1000))

    segment_tree = [0] * (2 ** int(np.log2(2*n-1) + 1))
    for i in range(len(array)):
        update(n, segment_tree, i, array[i])

    for _ in range(2000):
        if randint(1, 2) % 2 == 0:
            # query
            a = randint(0, n - 1)
            b = randint(a, n - 1)
            with_naive = naive_query(array, a, b)
            with_segment = query(n, segment_tree, a, b)
            assert with_segment == with_naive, \
                'naive={}, efficient={},\nn={},\na={}\nb={}\narray={}'.format(
                    with_naive,
                    with_segment,
                    n,
                    a,
                    b,
                    array
                )
        else:
            k = randint(0, n - 1)
            v = randint(1, 1000)
            naive_update(array, k, v)
            update(n, segment_tree, k, v)






















