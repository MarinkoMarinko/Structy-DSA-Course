from collections import deque

def largest_component(graph):
  visited = set()
  
  largest = 0
  for node in graph:
    size = explore_size(graph, node, visited)
    largest = max(largest, size)

  return largest


def explore_size(graph, node, visited):     # TC: O(e)
    if node in visited:                     # SC: O(n), where e is num of edges and n is num of nodes       
        return 0

    visited.add(node)

    size = 1
    for neighbor in graph[node]:
        size += explore_size(graph, neighbor, visited)

    return size


def explore_size(graph, node, visited):    # TC: O(e)
    if node in visited:                    # SC: O(n), where e is num of edges and n is num of nodes
        return 0
    visited.add(node)

    size = 0
    queue = deque([node])
    while queue:
        current = queue.popleft()
        size += 1
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        return size