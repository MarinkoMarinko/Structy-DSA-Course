def factorial(n):      # TC: O(n)
    if n == 0:           # SC: O(n), where n is the input
        return 1

    return n * factorial(n - 1)
