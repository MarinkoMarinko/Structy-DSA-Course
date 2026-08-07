def sum_possible(amount, numbers):                  # TC: O(a * n)
    return _sum_possible(amount, numbers, {})       # SC: O(a), where a is amount and n = len(numbers)


def _sum_possible(amount, numbers, memo):
    if amount == 0:
        return True

    if amount < 0:
        return False

    if amount in memo:
        return memo[amount]

    for num in numbers:
        if _sum_possible(amount - num, numbers, memo):
            memo[amount] = True
            return True

    memo[amount] = False
    return False