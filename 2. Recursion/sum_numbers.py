def sum_numbers_recursive(numbers):        # O(n^2) -> since we have around n + 1 calls and each call does O(n) amount of work, then O((n + 1) * n) = O(n^2)
  if len(numbers) == 0:
    return 0
  return numbers[0] + sum(numbers[1:])