def can_concat(s, words):                   # TC: O(s * w)
    return _can_concat(s, words, 0, {})     # TC: O(s), where s = len(s) and w = len(words)


def _can_concat(s, words, i, memo):
    if i in memo:
        return memo[i]

    if i >= len(s):
        return True

    for word in words:
        if s.startswith(word, i) and _can_concat(s, words, i + len(word), memo):
            memo[i] = True
            return True

    memo[i] = False
    return False
