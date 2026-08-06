from collections import deque

def closest_carrot(grid, starting_row, starting_col):       # TC: O(r * c)
    visited = set( [starting_row, starting_col] )           # SC: O(r * c), where r is num of rows and c is num of cols
    queue = deque([ (starting_row, starting_col, 0) ])
    while queue:
        row, col, distance = queue.popleft()

        if grid[row][col] == "C":
            return distance

        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for delta in deltas:
            dRow, dCol = delta
            neighborR = row + dRow
            neighborC = col + dCol
            row_inbounds = 0 <= neighborR < len(grid)
            col_inbounds = 0 <= neighborC < len(grid[0])
            neighborPos = (neighborR, neighborC)
            if neighborPos not in visited and row_inbounds and col_inbounds and grid[neighborR][neighborC] != "X":
                visited.add(neighborPos)
                queue.append((neighborR, neighborC, distance + 1))

    return -1