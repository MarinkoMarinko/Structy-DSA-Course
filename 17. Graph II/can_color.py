def can_color(graph):        # TC: O(e)
    coloring = {}            # SC: O(n), where e is num of edges and n is num of nodes
    for node in graph:
        if node not in coloring and not valid(graph, node, coloring, False):
            return False

    return True


def valid(graph, node, coloring, color):
    if node in coloring:
        return color == coloring[node]

    coloring[node] = color

    for neighbor in graph[node]:
        if not valid(graph, neighbor, coloring, not color):
            return False

    return True