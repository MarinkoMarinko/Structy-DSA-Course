def string_search(grid, s):             # TC: O(3^(r * c))
    for r in range(len(grid)):          # SC: O(r * c), where r is num of rows and c is num of cols
        for c in range(len(grid[0])):   
            if dfs(grid, r, c, s):
                return True

    return False


def dfs(grid, r, c, s):
    if len(s) == 0:
        return True

    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])
    if not row_inbounds or not col_inbounds:
        return False

    if grid[r][c] != s[0]:
        return False

    suffix = s[1:]
    char = grid[r][c]
    grid[r][c] = "*"
    result = dfs(grid, r + 1, c, suffix) or dfs(grid, r - 1, c, suffix) or dfs(grid, r, c + 1, suffix) or dfs(grid, r, c - 1, suffix)
    grid[r][c] = char
    return result