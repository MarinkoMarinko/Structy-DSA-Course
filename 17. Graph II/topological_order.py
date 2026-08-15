def topological_order(graph):  # TC: O(e + n)
    num_parents = {}             # SC: O(n), where e is num of edges and n is num of nodes
    for node in graph:
        num_parents[node] = 0

    for node in graph:
        for child in graph[node]:
            num_parents[child] += 1

    ready = [ node for node in graph if num_parents[node] == 0 ]
    result = []
    while ready:
        node = ready.pop()
        result.append(node)
        for child in graph[node]:
            num_parents[child] -= 1
            if num_parents[child] == 0:
                ready.append(child)

    return result