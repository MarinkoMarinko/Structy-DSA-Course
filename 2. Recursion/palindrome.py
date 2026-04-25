def palindrome(s):                      # O(n^2)
  if len(s) <= 1:
    return True
  elif s[0] != s[-1]:
    return False
  else:
    return palindrome(s[1:-1])
    