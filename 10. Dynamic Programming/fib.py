def fib(n):                # TC: O(n)
    return _fib(n, {})     # SC: O(n), where n is input

def _fib(n, memo):
    if n in [0, 1]:
        return n

    if n in memo:
        return memo[n]

    memo[n] = _fib(n - 1, memo) + _fib(n - 2, memo)
    return memo[n]