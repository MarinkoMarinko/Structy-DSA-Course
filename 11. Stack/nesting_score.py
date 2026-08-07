def nesting_score(string):      # TC: O(n)
    stack = [0]                 # SC: O(n), where n = len(string)

    for char in string:
        if char == "[":
            stack.append(0)
        else:
            popped = stack.pop()
            if popped == 0:
                stack[-1] += 1
            else:
                stack[-1] += 2 * popped

    return stack[0]