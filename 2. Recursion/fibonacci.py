def fibonacci(n):                                # Time complexity: O(2^n) -> for every function call, there are 2 additional calls 
                                                 # Space complexity: O(n)
  if n == 0 or n == 1:
    return n
  return fibonacci(n - 2) + fibonacci(n - 1)