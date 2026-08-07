def tribonacci(n):                  # TC: O(n)
    return _tribonacci(n, {})       # SC: O(n), where n is input
    


def _tribonacci(n, memo):        
    if n == 0 or n == 1:         
        return 0

    if n == 2:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = _tribonacci(n - 3, memo) + _tribonacci(n - 2, memo) + _tribonacci(n - 1, memo)
    return memo[n]