def tolerant_teams(rivalries):        # TC: O(e)
    graph = build_graph(rivalries)    # SC: O(n), where e is num of edges and n is num of nodes
    coloring = {}

    for node in graph:
        if node not in coloring and not is_tolerant(graph, node, coloring, False):
            return False

    return True


def is_tolerant(graph, node, coloring, color):
    if node in coloring:
        return color == coloring[node]

    coloring[node] = color

    for neighbor in graph[node]:
        if not is_tolerant(graph, neighbor, coloring, not color):
            return False

    return True


def build_graph(rivalries):
    graph = {}

    for rivarly in rivalries:
        a, b = rivarly
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph