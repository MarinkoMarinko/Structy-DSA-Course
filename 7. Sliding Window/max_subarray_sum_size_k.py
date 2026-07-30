def max_subarray_sum_size_k(nums, k):      # TC: O(n)
    current_sum = sum(nums[:k])            # SC: O(1), where n = len(nums)
    max_sum = current_sum

    for i in range(len(nums) - k):
        current_sum -= nums[i]
        current_sum += nums[i + k]

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum