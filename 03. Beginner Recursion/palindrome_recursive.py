def palindrome(s):          # TC: O(n^2)
    if len(s) in [0, 1]:    # SC: O(n^2), where n = len(s)
        return True

    if s[0] != s[-1]:
        return False

    return palindrome(s[1:-1])