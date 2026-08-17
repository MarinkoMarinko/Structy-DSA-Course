def max_value(nums):              # TC: O(n)
    max_val = float("-inf")       # SC: O(1), where n = len(nums)
    for num in nums:
        if num > max_val:
            max_val = num

    return max_val