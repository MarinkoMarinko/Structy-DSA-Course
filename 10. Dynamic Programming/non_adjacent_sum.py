def non_adjacent_sum(nums):                 # TC: O(n)
    return _non_adjacent_sum(nums, 0, {})   # SC: O(n), where n = len(nums)


def _non_adjacent_sum(nums, i, memo):
    if i in memo:
        return memo[i]

    if i >= len(nums):
        return 0

    inclusive = nums[i] + _non_adjacent_sum(nums, i + 2, memo)
    exclusive = _non_adjacent_sum(nums, i + 1, memo)

    memo[i] = max(inclusive, exclusive)
    return memo[i]