def has_cycle(graph):      # TC: O(e),
    visiting = set()       # SC: O(n), where e is num of edges and n is num of nodes
    visited = set()

    for node in graph:
        if _has_cycle(graph, node, visiting, visited):
            return True

    return False


def _has_cycle(graph, node, visiting, visited):
    if node in visited:
        return False

    if node in visiting:
        return True

    visiting.add(node)

    for neighbor in graph[node]:
        if _has_cycle(graph, neighbor, visiting, visited):
            return True

    visiting.remove(node)
    visited.add(node)
    return False