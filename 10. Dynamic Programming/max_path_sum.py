def max_path_sum(grid):                    # TC: O(r * c)
    return _max_path_sum(grid, 0, 0, {})   # SC: O(r * c), where r is num of rows and c is num of cols
  

def _max_path_sum(grid, r, c, memo): 
    pos = (r, c)
    if pos in memo:
        return memo[pos]

    if r == len(grid) or c == len(grid[0]):
        return float("-inf")

    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return grid[r][c]

    memo[pos] = grid[r][c] + max(_max_path_sum(grid, r + 1, c, memo), _max_path_sum(grid, r, c + 1, memo))
    return memo[pos]
