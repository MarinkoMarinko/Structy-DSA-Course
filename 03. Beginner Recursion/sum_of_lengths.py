def sum_of_lengths(strings):      # TC: O(n^2)
    if len(strings) == 0:         # SC: O(n^2), where n = len(strings)
        return 0

    return len(strings[0]) + sum_of_lengths(strings[1:])
