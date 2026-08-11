def find_min_index(nums):    # TC: O(logn)
    lo = 0                   # SC: O(1), where n = len(nums)
    hi = len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return lo

def binary_search(nums, target, lo, hi):
    while lo <= hi:
        mid = (lo + hi) // 2
        if target < nums[mid]:
            hi = mid - 1
        elif target > nums[mid]:
            lo = mid + 1
        else:
            return mid
        return -1

def find_in_rotated_sorted_array(nums, target):
    min_index = find_min_index(nums)
    left_result = binary_search(nums, target, 0, min_index - 1)
    right_result = binary_search(nums, target, min_index, len(nums) - 1)
    if left_result == -1:
        return right_result
    else:
        return left_result