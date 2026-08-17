from collections import deque, defaultdict

def best_house_build(grid):        # TC: O(r^2 * c^2)
    queue = deque()                # SC: O(r^2 * c^2)
    visited = defaultdict(set)
    total_distance = defaultdict(int)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                queue.append(((r, c, 0), (r, c)))
                visited[(r, c)].add((r, c))

    num_houses = len(queue)

    deltas = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    ]
    while len(queue):
        pos, src = queue.popleft()
        r, c, dist = pos
        for delta in deltas:
            delta_r, delta_c = delta
            new_r = r + delta_r
            new_c = c + delta_c
            new_pos = new_r, new_c
            r_inbounds = 0 <= new_r < len(grid)
            c_inbounds = 0 <= new_c < len(grid[0])
            if r_inbounds and c_inbounds and src not in visited[new_pos] and grid[new_r][new_c] == 0:
                visited[new_pos].add(src)
                queue.append(((new_r, new_c, dist + 1), src))
                total_distance[new_pos] += dist + 1

    min_dist = float("inf")
    for pos in visited:
        if len(visited[pos]) == num_houses:
            if total_distance[pos] > 0 and total_distance[pos] < min_dist:
                min_dist = total_distance[pos]
    return min_dist if min_dist != float('inf') else -1