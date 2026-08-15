def rare_routing(n, roads):          # TC: O(n^2)
    graph = make_graph(n, roads)     # SC: O(n^2), where n is num of nodes
    visited = set()
    valid = validate(graph, 0, visited, None)
    return valid and len(visited) == n

def validate(graph, node, visited, last_node):
    if node in visited:
        return False

    visited.add(node)
    for neighbor in graph[node]:
        if neighbor != last_node and not validate(graph, neighbor, visited, node):
            return False

    return True


def make_graph(n, roads):
    graph = {}
    for city in range(n):
        graph[city] = []

    for road in roads:
        a, b = road
        graph[a].append(b)
        graph[b].append(a)

    return graph