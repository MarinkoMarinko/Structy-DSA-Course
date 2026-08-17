from collections import Counter

def count_substring_at_most_k_distinct(s, k):  # TC: O(n)
    window_counter = Counter()                   # SC: O(k), where n = len(s) and k is the number of distinct chars (input)
    count_substrings = 0

    start = 0
    for end, leading_char in enumerate(s):
        window_counter[leading_char] += 1
        while len(window_counter) > k:
            trailing_char = s[start]
            window_counter[trailing_char] -= 1
            if window_counter[trailing_char] == 0:
                del window_counter[trailing_char]
            start += 1
            
        count_substrings += end - start + 1

    return count_substrings