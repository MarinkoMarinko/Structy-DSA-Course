from collections import deque

def island_count(grid):      # TC: O(r * c)
    visited = set()          # SC: O(r * c), where r is num of rows and c is num of cols

    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited):
                count += 1

    return count


def explore(grid, r, c, visited):
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])

    if not row_inbounds or not col_inbounds:
        return False

    if grid[r][c] == "W":
        return False

    pos = (r, c)
    if pos in visited:
        return False
    visited.add(pos)

    explore(grid, r - 1, c, visited)
    explore(grid, r + 1, c, visited)
    explore(grid, r, c - 1, visited)
    explore(grid, r, c + 1, visited)

    return True


def explore(grid, r, c, visited):
    pos = (r, c)
    if pos in visited or grid[r][c] == "W":
        return False
    visited.add(pos)

    deltas = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]
    queue = deque([ pos ])
    while queue:
        currentR, currentC = queue.popleft()
        for delta in deltas:
            dRow, dCol = delta
            neighborR = dRow + currentR
            neighborC = dCol + currentC
            row_inbounds = 0 <= neighborR < len(grid)
            col_inbounds = 0 <= neighborC < len(grid[0])
            neighborPos = (neighborR, neighborC)
            if neighborPos not in visited and row_inbounds and col_inbounds and grid[neighborR][neighborC] == "L":
                visited.add(neighborPos)
                queue.append(neighborPos)

    return True