def intersection(a, b):        # TC: O(n + m)
    set_a = set(a)             # SC: O(n), where n = len(a) and m = len(b)

    result = []
    for num in b:
        if num in set_a:
            result.append(num)

    return result