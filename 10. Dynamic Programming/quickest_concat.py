def quickest_concat(s, words):                  # TC: O(s * w)
    ans = _quickest_concat(s, words, 0, {})     # SC: O(s), where s = len(s) and w = len(words)
    if ans == float("inf"):
        return -1
    else:
        return ans


def _quickest_concat(s, words, i, memo):
    if i in memo:
        return memo[i]

    if i >= len(s):
        return 0

    min_words = float("inf")
    for word in words:
        if s.startswith(word, i):
            num_words = 1 + _quickest_concat(s, words, i + len(word), memo)
            min_words = min(min_words, num_words)

    memo[i] = min_words
    return min_words
