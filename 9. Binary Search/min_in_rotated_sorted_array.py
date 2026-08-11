def min_in_rotated_sorted_array(nums):    # TC: O(logn)
    lo = 0                                # SC: O(1), where n = len(nums)
    hi = len(nums) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid

    return nums[lo]