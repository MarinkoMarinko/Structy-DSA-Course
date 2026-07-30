from collections import Counter

def longest_two_char_substring(s):    # TC: O(n)
    longest = 0                       # SC: O(1), where n = len(s)
    window_counter = Counter()

    start = 0
    for end, leading_char in enumerate(s):
        window_counter[leading_char] += 1
        while len(window_counter) > 2:
            trailing_char = s[start]
            window_counter[trailing_char] -= 1
            if window_counter[trailing_char] == 0:
                del window_counter[trailing_char]
            start += 1
            
        if len(window_counter) == 2:
            longest = max(longest, end - start + 1)

    return longest
