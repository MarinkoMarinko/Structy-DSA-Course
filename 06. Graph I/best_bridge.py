from collections import deque

def best_bridge(grid):          # TC: O(r * c)
    main_island = None          # SC: O(r * c), where r is num of rows and c is num of cols
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            potentional_island = traverse_island(grid, r, c, set())
            if len(potentional_island) > 0:
                main_island = potentional_island
            break

    visited = set(main_island)
    queue = deque( [] )
    for pos in visited:
        r, c = pos
        queue.append((r, c, 0))

    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        r, c, distance = queue.popleft()

        if grid[r][c] == "L" and (r, c) not in main_island:
            return distance - 1

        for delta in deltas:
            delta_row, delta_col = delta
            neighborR = r + delta_row
            neighborC = c + delta_col
            neighborPos = (neighborR, neighborC)
            if inbounds(grid, neighborR, neighborC) and neighborPos not in visited:
                visited.add(neighborPos)
                queue.append((neighborR, neighborC, distance + 1))

    
def inbounds(grid, row, col):
    row_inbounds = 0 <= row < len(grid)
    col_inbounds = 0 <= col < len(grid[0])
    return row_inbounds and col_inbounds

def traverse_island(grid, r, c, visited):
    pos = (r, c)
    if pos in visited:
        return visited

    if not inbounds(grid, r, c) or grid[r][c] == "W":
        return visited

    visited.add(pos)

    traverse_island(grid, r - 1, c, visited)
    traverse_island(grid, r + 1, c, visited)
    traverse_island(grid, r, c - 1, visited)
    traverse_island(grid, r, c + 1, visited)

    return visited