def reverse_string(s):                        # O(n^2)
  if len(s) == 0:
    return ""
  return reverse_string(s[1:]) + s[0]