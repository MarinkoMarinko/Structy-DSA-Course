def find_subarray_sum(nums, target_sum):    # TC: O(n)
    window_sum = 0                          # SC: O(1), where n = len(nums)

    start = 0
    for end in range(len(nums)):
        window_sum += nums[end]
        while window_sum > target_sum:
            window_sum -= nums[start]
            start += 1
        
        if window_sum == target_sum:
            return (start, end)