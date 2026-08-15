def count_components(n, edges):
    roots = [ i for i in range(n) ]
    for edge in edges:
        a, b = edge
        union(roots, a, b)

    count = 0
    for i, node in enumerate(roots):
        if i == node:
            count += 1

    return count

def union(roots, node_a, node_b):
    root_a = find(roots, node_a)
    root_b = find(roots, node_b)

    if root_a == root_b:
        return

    roots[root_b] = root_a


def find(roots, node):
    if roots[node] == node:
        return node

    return find(roots, roots[node])


