def lowest_toll(highway_tolls, start_city, end_city):    # TC: O(n!)
    graph = build_graph(highway_tolls)                   # SC: O(n^2), where n is num of cities
    return min_path(graph, start_city, end_city, set())

def min_path(graph, start_city, end_city, visited):
    if start_city == end_city:
        return 0

    if start_city in visited:
        return float("inf")
    visited.add(start_city)

    min_cost = float("inf")
    for neighbor in graph[start_city]:
        cost = graph[start_city][neighbor]
        total_cost = cost + min_path(graph, neighbor, end_city, visited)
        min_cost = min(total_cost, min_cost)

    visited.remove(start_city)
    return min_cost
  

def build_graph(highway_tolls):
    graph = {}

    for road in highway_tolls:
        a, b, price = road
        if a not in graph:
            graph[a] = {}
        if b not in graph:
            graph[b] = {}
        graph[a][b] = price
        graph[b][a] = price

    return graph