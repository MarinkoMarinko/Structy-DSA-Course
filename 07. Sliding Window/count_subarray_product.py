def count_subarray_product(nums, target_product):    # TC: O(n)
    count = 0                                        # SC: O(1), where n = len(nums)
    window_prod = 1

    start = 0
    for end in range(len(nums)):
        window_prod *= nums[end]
        while window_prod >= target_product and start <= end:
            window_prod /= nums[start]
            start += 1

        count += end - start + 1

    return count