inf = 10 ** 20

class Edge:

    def __init__(self, start, end, length):
        self.start = start
        self.end = end
        self.length = length

    def __repr__(self):
        return '{} - {}~{}'.format(self.start, self.end, self.length)


def add_undirected(edges, a, b, length):
    edges.append(Edge(a, b, length))
    edges.append(Edge(b, a, length))


def get_shortest_path(n, edges, source, destination):

    dist = [inf] * (n + 1)
    pred = [-1] * (n + 1)
    dist[source] = 0
    for _ in range(n - 1):
        for e in edges:
            if dist[e.start] + e.length < dist[e.end]:
                dist[e.end] = dist[e.start] + e.length
                pred[e.end] = e.start

    path = []
    while pred[destination] != -1:
        length = dist[destination] - dist[pred[destination]]
        path.append(Edge(pred[destination], destination, length))
        destination = pred[destination]
    return path


def get_shortest_and_back(n, edges):
    shortest1 = get_shortest_path(n, edges, 1, n)
    new_edges = []
    for existing in edges:
        found_in_shortest = None
        for e in shortest1:
            if (e.start == existing.start and e.end == existing.end) or \
                    (e.start == existing.end and e.end == existing.start):
                found_in_shortest = e
                break
        if found_in_shortest and found_in_shortest.start == existing.start:
            new_edges.append(Edge(existing.end, existing.start, -existing.length))
        elif not found_in_shortest:
            new_edges.append(Edge(existing.start, existing.end, existing.length))

    shortest2 = get_shortest_path(n, new_edges, 1, n)
    return sum(e.length for e in shortest1) + sum(e.length for e in shortest2)



edges1 = []
add_undirected(edges1, 1, 2, 1)
add_undirected(edges1, 2, 3, 1)
add_undirected(edges1, 3, 4, 1)
add_undirected(edges1, 3, 5, 5)
add_undirected(edges1, 4, 8, 2)
add_undirected(edges1, 8, 12, 4)
add_undirected(edges1, 7, 8, 1)
add_undirected(edges1, 6, 7, 1)
add_undirected(edges1, 7, 11, 6)
add_undirected(edges1, 11, 12, 3)
add_undirected(edges1, 11, 10, 12)
add_undirected(edges1, 10, 6, 12)
add_undirected(edges1, 6, 5, 1)
add_undirected(edges1, 5, 9, 12)
add_undirected(edges1, 9, 10, 12)
add_undirected(edges1, 5, 1, 1)
result = get_shortest_and_back(12, edges1)
assert result == 21, 'got={}, expected={}'.format(result, 21)

edges2 = []
add_undirected(edges2, 1, 2, 1)
add_undirected(edges2, 2, 3, 1)
add_undirected(edges2, 2, 4, 2)
add_undirected(edges2, 3, 4, 1)
add_undirected(edges2, 1, 3, 2)
result = get_shortest_and_back(4, edges2)
assert result == 6, 'got={}, expected={}'.format(result, 6)

edges3 = []
add_undirected(edges3, 1, 2, 4)
add_undirected(edges3, 2, 3, 4)
add_undirected(edges3, 4, 3, 4)
add_undirected(edges3, 2, 4, 9)
add_undirected(edges3, 1, 4, 16)
add_undirected(edges3, 3, 1, 9)
result = get_shortest_and_back(4, edges3)
assert result == 26, 'got={}, expected={}'.format(result, 26)
