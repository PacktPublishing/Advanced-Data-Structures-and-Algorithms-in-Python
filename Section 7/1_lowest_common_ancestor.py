from random import randint
import numpy as np

inf = 10 ** 20


class Node:

    def __init__(self, label, children=None, parent=None):
        self.label = label
        if children:
            self.children = children
        else:
            self.children = []
        self.parent = parent


def euler_tour(node):
    if not node.children:
        return [node.label]

    result = [node.label]
    for child in node.children:
        result.extend(euler_tour(child))
        result.append(node.label)
    return result


print(euler_tour(
    Node(1, [
        Node(2, [
            Node(6, [
                Node(8),
                Node(7)
            ])
        ]),
        Node(3, [
            Node(4, [
                Node(5)
            ])
        ])
    ])
))


def get_depths(node):
    depth = {}

    def inner(node, d):
        depth[node.label] = d
        for child in node.children:
            inner(child, d + 1)
    inner(node, 0)
    return depth


def get_positions(euler):
    position = {}
    for i, v in enumerate(euler):
        if v not in position:
            position[v] = i
    return position


def query(array, segment_tree, a, b):
    def inner(node, left, right):
        if right < a or left > b:
            return None
        if a <= left and right <= b:
            return segment_tree[node]
        m = (left + right) // 2
        l_res = inner(2*node + 1, left, m)
        r_res = inner(2*node + 2, m + 1, right)
        if l_res is None:
            return r_res
        if r_res is None:
            return l_res
        if array[l_res] < array[r_res]:
            return l_res
        return r_res
    return inner(0, 0, len(array) - 1)


def build(array):
    n = len(array)
    segment_tree = [None] * (2 ** int(np.log2(2*n - 1) + 1))

    def inner(node, left, right):
        if left == right:
            segment_tree[node] = left
            return

        m = (left + right) // 2
        inner(2*node + 1, left, m)
        inner(2*node + 2, m + 1, right)
        l_res = segment_tree[2*node + 1]
        r_res = segment_tree[2*node + 2]
        if array[l_res] < array[r_res]:
            segment_tree[node] = l_res
        else:
            segment_tree[node] = r_res
    inner(0, 0, n - 1)
    return segment_tree


def get_random_tree(n):
    label = 2

    def inner(node):
        nonlocal label
        children = min(randint(1, 4), n - label + 1)
        for _ in range(children):
            node.children.append(Node(label, parent=node))
            label += 1
        for c in node.children:
            if label <= n:
                inner(c)
        return node

    ret = inner(Node(1, parent=None))
    assert label - 1 == n, 'label={}, n={}'.format(label, n)
    return ret


def find_node(node, label):
    if node.label == label:
        return node
    for c in node.children:
        found = find_node(c, label)
        if found:
            return found
    return None


for t in range(100):

    n = randint(100, 1000)
    tree = get_random_tree(n)

    num_queries = randint(10, 100)
    depth = get_depths(tree)
    euler = euler_tour(tree)
    position = get_positions(euler)
    euler_depth = [depth[e] for e in euler]
    segment_tree = build(euler_depth)
    for _ in range(num_queries):
        a = randint(1, n)
        b = randint(1, n)
        pa, pb = position[a], position[b]
        if pa > pb:
            pa, pb = pb, pa
        q = query(euler_depth, segment_tree, pa, pb)

        t1 = find_node(tree, a)
        t2 = find_node(tree, b)
        v1 = {}
        v2 = {}
        answer = None
        while True:
            if t1:
                v1[t1.label] = True
            if t2:
                v2[t2.label] = True
            if t1 and t1.label in v2:
                answer = t1.label
                break
            if t2 and t2.label in v1:
                answer = t2.label
                break

            if t1:
                t1 = t1.parent
            if t2:
                t2 = t2.parent

        assert answer == euler[q], \
            'euler_depth[q]={}\n' \
            'euler[q]={}\n' \
            'depth[euler[q]]={}\n' \
            'naive={}\n' \
            'n={}\n' \
            'len(euler)={}\n' \
            'a={}, b={},\n' \
            'pa={}, pb={}\n' \
            'euler_depth[pa]={}, euler_depth[pb]={}\n' \
            'naive min={}\n' \
            'segment_tree={}\n'.format(
                euler_depth[q],
                euler[q],
                depth[euler[q]],
                answer,
                n,
                len(euler),
                a, b,
                pa, pb,
                euler_depth[pa], euler_depth[pb],
                euler[np.argmin(euler_depth[pa:pb+1])],
                segment_tree
        )


