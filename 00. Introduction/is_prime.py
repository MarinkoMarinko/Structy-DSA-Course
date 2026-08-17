import math

def is_prime(n):      # TC: O(sqrt(n))
  if n < 2:           # SC: O(1), where n is the input
    return False

  for i in range(2, math.floor(math.sqrt(n)) + 1):
    if n % i == 0:
      return False

  return True