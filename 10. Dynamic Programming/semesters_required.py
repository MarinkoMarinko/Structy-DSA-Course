def semesters_required(num_courses, prereqs):      # TC: O(p)
    graph = build_graph(num_courses, prereqs)      # SC: O(e), where p is num of prereqs and n is num of courses
    distance = {}
    for course in range(num_courses):
        if len(graph[course]) == 0:
            distance[course] = 1

    for course in range(num_courses):
        traverse(graph, course, distance)

    return max(distance.values())


def build_graph(num_courses, prereqs):
    graph = {}

    for i in range(num_courses):
        graph[i] = []

    for prereq in prereqs:
        a, b = prereq
        graph[a].append(b)

    return graph


def traverse(graph, node, distance):
    if node in distance:
        return distance[node]

    max_distance = 0
    for neighbor in graph[node]:
        neighbor_distance = traverse(graph, neighbor, distance)
        if neighbor_distance > max_distance:
            max_distance = neighbor_distance

    distance[node] = 1 + max_distance
    return distance[node]