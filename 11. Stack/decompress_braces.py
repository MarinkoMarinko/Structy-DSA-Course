def decompress_braces(string):      # TC: O(9^m * s)
    numbers = "123456789"           # SC: O(9^m * s), where s = len(string) and m is count of brace pairs
    stack = []
    for ch in string:
        if ch in numbers:
            stack.append(int(ch))
        else:
            if ch == "}":
                segment = ""
                while isinstance(stack[-1], str):
                    popped = stack.pop()
                    segment = popped + segment
                num = stack.pop()
                stack.append(segment * num)
            elif ch != "{":
                stack.append(ch)

    return "".join(stack)