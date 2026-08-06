from collections import deque

def connected_components_count(graph):
    visited = set()

    count = 0
    for node in graph:
        if explore(graph, node, visited):
            count += 1

    return count


def explore(graph, node, visited):    # TC: O(e)
    if node in visited:               # SC: O(n), where e is num of edges and n is num of nodes
        return False

    visited.add(node)

    for neighbor in graph[node]:
        explore(graph, neighbor, visited)

    return True

def explore(graph, src, visited):    # TC: O(e)
    if src in visited:               # SC: O(n), where e is num of edges and n is num of nodes
        return False

    visited.add(src)

    queue = deque([src])

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return True