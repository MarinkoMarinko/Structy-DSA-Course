def knightly_number(n, m, kr, kc, pr, pc):              # TC: O(m * n^2)
    return _knightly_number(n, m, kr, kc, pr, pc, {})   # SC: O(m * n^2), where n is length of board and m is num of moves

def _knightly_number(n, m, kr, kc, pr, pc, memo):
    key = (m, kr, kc)

    if key in memo:
        return memo[key]

    if kr < 0 or kr >= n or kc < 0 or kc >= n:
        return 0

    if m == 0:
        if (kr, kc) == (pr, pc):
            return 1
        else:
            return 0

    neighbors = [
        ( kr + 2, kc + 1 ),
        ( kr - 2, kc + 1 ),
        ( kr + 2, kc - 1 ),
        ( kr - 2, kc - 1 ),
        ( kr + 1, kc + 2 ),
        ( kr - 1, kc + 2 ),
        ( kr + 1, kc - 2 ),
        ( kr - 1, kc - 2 ),
    ]

    count = 0
    for neighbor in neighbors:
        neighbor_r, neighbor_c = neighbor
        count += _knightly_number(n, m - 1, neighbor_r, neighbor_c, pr, pc, memo)

    memo[key] = count
    return count