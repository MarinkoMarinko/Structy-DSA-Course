def longest_subarray_sum(nums, target_sum):    # TC: O(n)
    max_len = -1                               # SC: O(1), where n = len(nums)
    window_sum = 0
    start = 0
    for end in range(len(nums)):
        window_sum += nums[end]
        while window_sum > target_sum:
            window_sum -= nums[start]
            start += 1

        if window_sum == target_sum:
            current_len = end - start + 1
            if current_len > max_len:
                max_len = current_len

    return max_len 
