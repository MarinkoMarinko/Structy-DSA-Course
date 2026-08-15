from collections import deque

def knight_attack(n, kr, kc, pr, pc):    # TC: O(n^2)
    visited = set()                      # SC: O(n^2), where n = len(board)
    visited.add( (kr, kc) )
    queue = deque([ (kr, kc, 0) ])
    while queue:
        r, c, step = queue.popleft()
        if (r, c) == (pr, pc):
            return step

        neighbors = get_moves(n, r, c)
        for neighbor in neighbors:
            neighbor_r, neigbor_c = neighbor
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor_r, neigbor_c, step + 1))
    return None

def get_moves(n, r, c):
    positions = [
    ( r - 1, c - 2 ),
    ( r + 1, c - 2 ),
    ( r + 2, c - 1 ),
    ( r + 2, c + 1 ),
    ( r - 1, c + 2 ),
    ( r + 1, c + 2 ),
    ( r - 2, c - 1 ),
    ( r - 2, c + 1 )
    ]

    inbound = []
    for pos in positions:
        row, col = pos
        if 0 <= row < n and 0 <= col < n:
            inbound.append(pos)

    return inbound