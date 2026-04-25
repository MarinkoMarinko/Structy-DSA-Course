def sum_of_lengths(strings):            # O(n^2)
  if len(strings) == 0:
    return 0
  return len(strings[0]) + sum_of_lengths(strings[1:])