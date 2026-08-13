def possible_paths(graph, src, dst):            # TC: O(n *2 ^n)
    paths = _possible_paths(graph, src, dst)    # SC: O(n * 2^n), where n is num of nodes
    return [path[::-1] for path in paths]

def _possible_paths(graph, src, dst):
    if src == dst:
        return [ [dst] ]

    paths = []
    for neighbor in graph[src]:
        neighbor_paths = _possible_paths(graph, neighbor, dst)
        for neighbor_path in neighbor_paths:
            neighbor_path.append(src)
            paths.append(neighbor_path)

    return paths