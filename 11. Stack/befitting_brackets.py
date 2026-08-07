def befitting_brackets(string):    # TC: O(n)
    stack = []                     # SC: O(n), where n = len(string)

    brackets = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    for ch in string:
        if ch in brackets:
            stack.append(brackets[ch])
        else:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                return False
        
    return len(stack) == 0