def create_combinations(items, k):    # TC: ~O(n choose k)
    if k == 0:                        # SC: ~O(n choose k), where n = len(items) and k = target length
        return [ [] ]

    if len(items) < k:
        return []

    first = items[0]
    combos_with_first = []
    for combo in create_combinations(items[1:], k - 1):
        combos_with_first.append([ first, *combo ])

    combos_without_first = create_combinations(items[1:], k)
    return combos_with_first + combos_without_first