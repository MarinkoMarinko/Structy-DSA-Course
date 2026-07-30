def exclusive_items(a, b):    # TC: O(n + m)
    set_a = set(a)            # SC: O(n + m), where n = len(a) and b = len(b)
    set_b = set(b)

    result = []
    for num in a:
        if num not in set_b:
            result.append(num)

    for num in b:
        if num not in set_a:
            result.append(num)

    return result