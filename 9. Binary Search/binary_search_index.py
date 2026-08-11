def binary_search_index(nums, target):    # TC: O(logn)
    lo = 0                                # SC: O(1), where n = len(nums)
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if target < nums[mid]:
            hi = mid - 1
        elif target > nums[mid]:
            lo = mid + 1
        else:
            return mid

    return lo