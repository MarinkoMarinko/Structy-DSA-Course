def find_leftmost_index(nums, target):    # TC: O(logn)
    leftmost = -1                         # SC: O(1), where n = len(nums)

    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if target < nums[mid]:
            hi = mid - 1
        elif target > nums[mid]:
            lo = mid + 1
        else:
            leftmost = mid
            hi = mid - 1

    return leftmost