import math

def max_subarray_product_size_k(nums, k):    # TC: O(n),
    current_prod = math.prod(nums[:k])       # SC: O(1), where n = len(nums)
    max_prod = current_prod

    for i in range(len(nums) - k):
        current_prod /= nums[i]
        current_prod *= nums[i + k]

    if current_prod > max_prod:
        max_prod = current_prod

    return max_prod