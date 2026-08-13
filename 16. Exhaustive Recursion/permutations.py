def permutations(items):      # TC: ~O(n!)
    if not items:             # SC: ~O(n!), where n = len(items)
        return [ [] ]

    first = items[0]
    perms_without_first = permutations(items[1:])

    all_perms = []
    for perm in perms_without_first:
        for i in range(len(perm) + 1):
            all_perms.append([*perm[:i], first, *perm[i:]])

    return all_perms