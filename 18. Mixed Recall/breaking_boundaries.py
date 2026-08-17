def breaking_boundaries(m, n, k, r, c):                # TC: O(m * n * k)
    return _breaking_boundaries(m, n, k, r, c, {})     # SC: O(m * n * k), where m is num of rows, n is num of cols and k is num of moves


def _breaking_boundaries(m, n, k, r, c, memo):
    key = (k, r, c)

    if key in memo:
        return memo[key]

    if not inbounds(m, n, r, c):
        return 1

    if k == 0:
        return 0

    count = 0

    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for delta in deltas:
        d_row, d_col = delta
        neighbor_r = r + d_row
        neighbor_c = c + d_col
        count += _breaking_boundaries(m, n, k - 1, neighbor_r, neighbor_c, memo)

    memo[key] = count
    return count


def inbounds(m, n, r, c):
    return 0 <= r < m and 0 <= c < n
