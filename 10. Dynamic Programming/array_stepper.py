def array_stepper(numbers):                  # TC" O(n^2)
    return _array_stepper(numbers, 0, {})    # SC: O(n), where n = len(numbers)

def _array_stepper(numbers, i, memo):
    if i in memo:
        return memo[i]

    if i >= len(numbers) - 1:
        return True

    max_step = numbers[i]
    for step in range(1, max_step + 1):
        if _array_stepper(numbers, i + step, memo):
            memo[i] = True
            return True

    memo[i] = False
    return False