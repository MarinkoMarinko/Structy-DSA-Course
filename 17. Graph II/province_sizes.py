def province_sizes(n, roads):          # TC: ~O(n + e)
    roots = [ i for i in range(n) ]    # SC: O(n), where n is num of cities and e is num of roads
    sizes = [ 1 for _ in range(n) ]

    for road in roads:
        a, b = road
        union(roots, sizes, a, b)

    result = []
    for i, root in enumerate(roots):
        if i == root:
            result.append(sizes[i])

    return result


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