def token_transform(s, tokens):      # TC: O(n^m)
    i = 0                            # SC: O(n^m), where n = len(s) and m is num of unique tokens
    j = 1

    result = []
    while i < len(s):
        if s[i] != "$":
            result.append(s[i])
            i += 1
            j = i + 1
        elif s[j] != "$":
            j += 1
        else:
            key = s[i:j + 1]
            val = tokens[key]
            evaluated = token_transform(val, tokens)
            tokens[key] = evaluated
            result.append(evaluated)
            i = j + 1
            j = i + 1

    return "".join(result)