def has_substring_anagram(s, anagram):  # TC: O(n * k)
    anagram_set = set(anagram)          # SC: O(k), where n = len(s) and k = len(anagram)
    window_set = set(s[:len(anagram)])
    if anagram_set == window_set:
        return True

    for i in range(len(s) - len(anagram)):
        window_set.remove(s[i])
        window_set.add(s[i + len(anagram)])

        if anagram_set == window_set:
            return True

    return False