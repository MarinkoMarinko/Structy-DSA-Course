def paired_parentheses(string):      # TC: O(n)
    open_counter = 0                 # SC: O(1), where n = len(string)
    for ch in string:
        if ch == "(":
            open_counter += 1
        elif ch == ")":
            if open_counter == 0:
                return False
            open_counter -= 1

    return open_counter == 0