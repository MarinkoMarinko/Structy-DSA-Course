def parenthetical_possibilities(s):    # TC: ~O(m ^ n)
    if len(s) == 0:                    # SC: ~O(m ^ n), where m = len of largest parenthetical group and n = len(s)
        return [""]

    result = []
    choices, remaining = get_choices(s)
    for choice in choices:
        remainder_pos = parenthetical_possibilities(remaining)
        for pos in remainder_pos:
            result.append(choice + pos)

    return result

def get_choices(s):
    if s[0] == "(":
        end = s.index(")")
        chars = s[1:end]
        remaining = s[end + 1:]
    else:
        chars = s[0]
        remaining = s[1:]
        return (chars, remaining)