def subarray_target_sum_size_k(nums, target, k):    # TC: O(n)
    current_sum = sum(nums[:k])                     # SC: O(1), where n = len(nums)
    count = 1 if current_sum == target else 0

    for i in range(len(nums) - k):
        current_sum -= nums[i]
        current_sum += nums[i + k]

    if current_sum == target:
        count += 1

    return count