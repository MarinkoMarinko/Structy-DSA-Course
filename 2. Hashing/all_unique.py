def all_unique(items):        # TC: O(n)
    items_set = set(items)    # SC: O(n), where n = len(items)
    return len(items_set) == len(items)