from collections import Counter

def count_substring_anagrams(s, anagram):    # TC: O(n * k)
    anagram_counter = Counter(anagram)       # SC: O(k), where n = len(s) and k = len(anagram)
    window_counter = Counter(s[:len(anagram)])

    count = 1 if window_counter == anagram_counter else 0
    for i in range(len(s) - len(anagram)):
        window_counter[s[i]] -= 1
        window_counter[s[i + len(anagram)]] += 1
        if window_counter == anagram_counter:
            count += 1

    return count