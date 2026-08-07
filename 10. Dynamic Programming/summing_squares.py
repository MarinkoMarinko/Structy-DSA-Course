import math

def summing_squares(n):                 # TC: O(n * sqrt(n))
    return _summing_squares(n, {})      # SC: O(n), where n = len(nums)

def _summing_squares(n, memo):
    if n in memo:
        return memo[n]

    if n == 0:
        return 0

    if n < 0:
        return float("inf")

    min_squares = float("inf")
    for i in range(1, math.floor(math.sqrt(n)) + 1):
        square = i * i
        count_square = 1 + _summing_squares(n - square, memo)
        min_squares = min(min_squares, count_square)

    memo[n] = min_squares
    return min_squares