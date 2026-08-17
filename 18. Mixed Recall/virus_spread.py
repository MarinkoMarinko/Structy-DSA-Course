from collections import deque

def virus_spread(grid):        # TC: O(r * c)
    clean_computers = 0        # SC: O(r * c), where r is num of rows and c is num of cols
    queue = deque([])
    visited = set()

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                clean_computers += 1
            elif grid[r][c] == 2:
                queue.append((r, c, 0))
                visited.add((r, c))

    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    max_time = 0
    while queue:
        r, c, time = queue.popleft()
        max_time = time
        for delta in deltas:
            delta_r, delta_c = delta
            neighbor_r = r + delta_r
            neighbor_c = c + delta_c
            neighbor_pos = (neighbor_r, neighbor_c)
            if inbounds(grid, neighbor_r, neighbor_c) and grid[neighbor_r][neighbor_c] != 0 and neighbor_pos not in visited:
                clean_computers -= 1
                visited.add(neighbor_pos)
                queue.append((*neighbor_pos, time + 1))

    return -1 if clean_computers > 0 else max_time


def inbounds(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])