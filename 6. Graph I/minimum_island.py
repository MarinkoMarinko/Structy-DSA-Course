from collections import deque

def minimum_island(grid):        # TC: O(r * c)
    min_size = float("inf")      # SC: O(r * c), where r is num of rows and c is num of cols

    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = explore_size(grid, r, c, visited)
            if size > 0 and size < min_size:
                min_size = size

    return min_size


def explore_size(grid, r, c, visited):
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])

    if not row_inbounds or not col_inbounds:
        return 0

    if grid[r][c] == "W":
        return 0

    pos = (r, c)
    if pos in visited:
        return 0
    visited.add(pos)

    size = 1
    size += explore_size(grid, r - 1, c, visited)
    size += explore_size(grid, r + 1, c, visited)
    size += explore_size(grid, r, c - 1, visited)
    size += explore_size(grid, r, c + 1, visited)

    return size


def explore_size(grid, r, c, visited):
    pos = (r, c)
    if pos in visited or grid[r][c] == "W":
        return 0
    visited.add(pos)

    deltas = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]
    queue = deque([ pos ])
    size = 0
    while queue:
        currentR, currentC = queue.popleft()
        size += 1
        for delta in deltas:
            deltaR, deltaC = delta
            neighborR = deltaR + currentR
            neighborC = deltaC + currentC
            row_inbounds = 0 <= neighborR < len(grid)
            col_inbounds = 0 <= neighborC < len(grid[0])
            neighborPos = (neighborR, neighborC)
            if neighborPos not in visited and row_inbounds and col_inbounds and grid[neighborR][neighborC] == "L":
                visited.add(neighborPos)
                queue.append(neighborPos)

    return size