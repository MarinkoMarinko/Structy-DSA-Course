def counting_change(amount, coins):                  # TC: O(a * c)
    return _counting_change(amount, coins, 0, {})    # SC: O(a * c), where a is amount and c = len(coins)

def _counting_change(amount, coins, i, memo):
    key = (amount, i)
    if key in memo:
        return memo[key]

    if amount == 0:
        return 1

    if i >= len(coins):
        return 0

    coin = coins[i]

    total_ways = 0
    for qty in range(0, amount // coin + 1):
        remainder = amount - qty * coin
        total_ways += _counting_change(remainder, coins, i + 1, memo)

    memo[key] = total_ways
    return total_ways