def weighted_graph_min_path(graph, src, dst):                # TC: O(n!)
    return _weighted_graph_min_path(graph, src, dst, set())  # SC: O(n), where n is num of nodes


def _weighted_graph_min_path(graph, src, dst, visited):
    if src == dst:
        return 0

    if src in visited:
        return float("inf")

    visited.add(src)

    min_cost = float("inf")
    for neighbor in graph[src]:
        cost = graph[src][neighbor]
        total_cost = cost + _weighted_graph_min_path(graph, neighbor, dst, visited)
        min_cost = min(min_cost, total_cost)

    visited.remove(src)
    return min_cost