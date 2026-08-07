def reverse_some_chars(s, chars):      # TC: O(n + m)
    char_set = set(chars)              # SC: O(n + m), where n = len(s) and m = len(chars)

    stack = []
    for ch in s:
        if ch in char_set:
            stack.append(ch)

    result = []
    for ch in s:
        if ch in char_set:
            result.append(stack.pop())
        else:
            result.append(ch)

    return "".join(result)