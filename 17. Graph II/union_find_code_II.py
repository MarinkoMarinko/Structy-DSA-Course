def count_components(n, edges):        # TC: O(n + e)
    roots = [ i for i in range(n) ]    # SC: O(n), where n is num of nodes and e is num of edges
    sizes = [ 1 for _ in range(n) ]

    for edge in edges:
        a, b = edge
        union(roots, sizes, a, b)

    count = 0
    for i, node in enumerate(roots):
        if i == node:
            count += 1

    return count

def union(roots, sizes, node_a, node_b):
    root_a = find(roots, node_a)
    root_b = find(roots, node_b)

    if root_a == root_b:
        return

    if sizes[root_a] >= sizes[root_b]:
        roots[root_b] = root_a
        sizes[root_a] += sizes[root_b]
    else:
        roots[root_a] = root_b
        sizes[root_b] += sizes[root_a]


def find(roots, node):
    if roots[node] == node:
        return node

    found = find(roots, roots[node])
    roots[node] = found
    return found