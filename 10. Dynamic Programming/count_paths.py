def count_paths(grid):                      # TC: O(r * c)
    return _count_paths(grid, 0, 0, {})     # SC: O(r * c), where r is num of rows and c is num of cols


def _count_paths(grid, r, c, memo):
    pos = (r, c)
    if pos in memo:
        return memo[pos]

    if r == len(grid) or c == len(grid[0]) or grid[r][c] == "X":
        return 0

    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return 1

    memo[pos] = _count_paths(grid, r, c + 1, memo) + _count_paths(grid, r + 1, c, memo)

    return memo[pos]
