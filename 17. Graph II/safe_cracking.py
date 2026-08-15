def safe_cracking(hints):           # TC: O(n)
    graph = build_graph(hints)      # SC: O(n), where n is num of hints
    return topological_order(graph)


def topological_order(graph):
    num_parents = {}
    for node in graph:
        num_parents[node] = 0

    for node in graph:
        for child in graph[node]:
            num_parents[child] += 1

    ready = [ node for node in num_parents if num_parents[node] == 0 ]
    result = []
    while ready:
        current_node = ready.pop()
        result.append(str(current_node))
        for child in graph[current_node]:
            num_parents[child] -= 1
            if num_parents[child] == 0:
                ready.append(child)

    return "".join(result)

def build_graph(hints):
    graph = {}
    for hint in hints:
        a, b = hint
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)

    return graph