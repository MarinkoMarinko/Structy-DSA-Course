def all_trips(routes, start_station, end_station):      # TC: O(2^n)
    graph = make_graph(routes)                          # SC: O(2^n), where n is num of bus stops
    all_paths = _all_trips(graph, start_station, end_station)
    return [ path[::-1] for path in all_paths ]


def _all_trips(graph, src, dst):
    if src == dst:
        return [ [src] ]

    all_paths = []
    for neighbor in graph[src]:
        neighbor_paths = _all_trips(graph, neighbor, dst)
        for neighbor_path in neighbor_paths:
            neighbor_path.append(src)
            all_paths.append(neighbor_path)

    return all_paths


def make_graph(routes):
    graph = {}
    for route in routes:
        a, b = route
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)

    return graph