def extra_cable(num_computers, cables):            # TC: O(n + e)
    roots = [ i for i in range(num_computers) ]    # SC: O(n), where n is num of computers and e is num of cables
    sizes = [ 1 for _ in range(num_computers) ]

    for cable in cables:
        a, b = cable
        if not union(roots, sizes, a, b):
            return cable


def union(roots, sizes, node_a, node_b):
    root_a = find(roots, node_a)
    root_b = find(roots, node_b)

    if root_a == root_b:
        return False

    if sizes[root_a] >= sizes[root_b]:
        roots[root_b] = root_a
        sizes[root_a] += sizes[root_b]
    else:
        roots[root_a] = root_b
        sizes[root_b] += sizes[root_a]

    return True

def find(roots, node):
    if node == roots[node]:
        return node

    found = find(roots, roots[node])
    roots[node] = found
    return found
  