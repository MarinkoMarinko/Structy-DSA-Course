def count_in_sorted_array(nums, target):            # TC: O(logn)
    leftmost = find_leftmost_index(nums, target)    # SC: O(1), where n = len(nums)
    rightmost = find_rightmost_index(nums, target)

    if leftmost == -1:
        return 0
    return rightmost - leftmost + 1


def find_leftmost_index(nums, target):
    leftmost = -1

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


def find_rightmost_index(nums, target):
    rightmost = -1

    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if target < nums[mid]:
            hi = mid - 1
        elif target > nums[mid]:
            lo = mid + 1
        else:
            rightmost = mid
            lo = mid + 1

    return rightmost