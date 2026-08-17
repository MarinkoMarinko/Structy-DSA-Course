from collections import deque

def has_path(graph, src, dst):      # TC: O(e)
    if src == dst:                  # SC: O(n), where e is num of edges and n is number of nodes
        return True

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst):
            return True

    return False

def has_path(graph, src, dst):      # TC: O(e)
    nodes = deque([ src ])          # SC: O(n), where e is num of edges and n is number of nodes
    while nodes:
        val = nodes.popleft()
        if val == dst:
            return True

        for neighbor in graph[val]:
            nodes.append(neighbor)

    return False