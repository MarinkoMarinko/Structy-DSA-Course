def reverse_string(s):      # TC: O(n^2)
    if len(s) == 0:         # SC: O(n^2), where n = len(s)
        return ""

    return reverse_string(s[1:]) + s[0]