def max_ones_with_single_flip(s):    # TC: O(n)
    longest = 0                      # SC: O(1), where n = len(s)
    zero_count = 0

    start = 0
    for end in range(len(s)):
        if s[end] == "0":
            zero_count += 1
        while zero_count > 1:
            if s[start] == "0":
                zero_count -= 1
            start += 1

    longest = max(longest, end - start + 1)

    return longest
    