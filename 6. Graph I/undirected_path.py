from collections import deque

def undirected_path(edges, node_A, node_B):      # TC: O(e)
    graph = build_graph(edges)                   # SC: O(e), where e is num of edges
    visited = set()
    return has_path(graph, node_A, node_B, visited)

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

def undirected_path(edges, node_A, node_B):      # TC: O(e)
    graph = build_graph(edges)                   # SC: O(e), where e is num of edges
    visited = set()
    return has_path(graph, node_A, node_B)
  
def has_path(graph, src, dst, visited):
    if src == dst:
        return True

    if src in visited:
        return False

    visited.add(src)

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst, visited):
            return True

    return False


def has_path(graph, src, dst):
    visited = { src }
    queue = deque([ src ])
    while queue:
        node = queue.popleft()
        if node == dst:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return False