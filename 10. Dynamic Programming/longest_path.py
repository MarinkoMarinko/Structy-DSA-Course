def longest_path(graph):      # TC: O(e)
    distance = {}             # SC: O(n), where e is num of edges and n is num of nodes
    for node in graph:
        if len(graph[node]) == 0:
            distance[node] = 0

    for node in graph:
        traverse(graph, node, distance)

    return max(distance.values())

  
def traverse(graph, node, distance):
    if node in distance:
        return distance[node]

    largest = 0
    for neighbor in graph[node]:
        attempt = traverse(graph, neighbor, distance)
        largest = max(largest, attempt)

    distance[node] = 1 + largest
    return distance[node]