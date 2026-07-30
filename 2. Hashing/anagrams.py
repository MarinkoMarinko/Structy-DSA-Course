from collections import Counter

def anagrams(s1, s2):                  # TC: O(n + m)
    return Counter(s1) == Counter(s2)  # SC: O(n + m), where n = len(s1) and m = len(s2)