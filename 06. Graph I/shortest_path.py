from collections import deque

def shortest_path(edges, node_A, node_B):       # TC: O(e)
    graph = build_graph(edges)                  # SC: O(e), where e is num of edges
    visited = set(node_A)
    queue = deque([ (node_A, 0) ])
    while queue:
        node, distance = queue.popleft()
        if node == node_B:
            return distance

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(node)
                queue.append((neighbor, distance + 1))

    return -1

def build_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph