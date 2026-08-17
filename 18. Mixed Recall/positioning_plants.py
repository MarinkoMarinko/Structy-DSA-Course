def positioning_plants(costs):                          # TC: O(n * m)
    return _positioning_plants(costs, 0, None, {})      # SC: O(n * m), where n is num of garden pos (rows) and m is num of plant types (cols)


def _positioning_plants(costs, pos, last_plant, memo):
    key = (pos, last_plant)

    if key in memo:
        return memo[key]

    if pos == len(costs):
        return 0

    min_cost = float("inf")
    for plant, cost in enumerate(costs[pos]):
        if plant != last_plant:
            current = cost + _positioning_plants(costs, pos + 1, plant, memo)
            min_cost = min(min_cost, current)

    memo[key] = min_cost
    return min_cost