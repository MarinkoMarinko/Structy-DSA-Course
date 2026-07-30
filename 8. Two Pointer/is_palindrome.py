def is_palindrome(s):      # TC: O(n)
    i = 0                  # SC: O(1), where n = len(s)
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True