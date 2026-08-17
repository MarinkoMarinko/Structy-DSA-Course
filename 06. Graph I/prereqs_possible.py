def prereqs_possible(num_courses, prereqs):         # TC: O(n + p)
    graph = build_graph(num_courses, prereqs)       # SC: O(n + p), where n is num of courses and p is num of prereqs

    visiting = set()
    visited = set()
    for node in graph:
        if has_cycle(graph, node, visiting, visited):
            return False

    return True


def has_cycle(graph, node, visiting, visited):
    if node in visited:
        return False

    if node in visiting:
        return True

    visiting.add(node)

    for neighbor in graph[node]:
        if has_cycle(graph, neighbor, visiting, visited):
            return True

    visiting.remove(node)
    visited.add(node)
    return False

def build_graph(num_courses, prereqs):
    graph = {}
    for i in range(num_courses):
        graph[i] = []

    for req in prereqs:
        a, b = req
        graph[a].append(b)

    return graph