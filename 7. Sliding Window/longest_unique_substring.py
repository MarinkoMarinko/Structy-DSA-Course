from collections import Counter

def longest_unique_substring(s):    # TC: O(n)
    longest = 0                     # SC: O(n), where n = len(s)
    window_counter = Counter()

    start = 0
    for end in range(len(s)):
        window_counter[s[end]] += 1
        while window_counter[s[end]] > 1:
            window_counter[s[start]] -= 1
            start += 1

        longest = max(end - start + 1, longest)

    return longest