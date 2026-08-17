def knapsack(values, weights, weight_limit):                # TC: O(n * w)
    return _knapsack(values, weights, weight_limit, 0, {})  # SC: O(n * w), where n is num of items and w is weight limit


def _knapsack(values, weights, weight_limit, i, memo):
    key = (i, weight_limit)

    if key in memo:
        return memo[key]

    if weight_limit < 0:
        return float("-inf")

    if i == len(values):
        return 0

    without_first = _knapsack(values, weights, weight_limit, i + 1, memo)
    with_first = values[i] + _knapsack(values, weights, weight_limit - weights[i], i + 1, memo)

    memo[key] = max(with_first, without_first)
    return memo[key]