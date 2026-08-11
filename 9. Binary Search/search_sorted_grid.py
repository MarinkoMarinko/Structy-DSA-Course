def search_sorted_grid(grid, target):    # TC: O(log(n * m))
    r = find_row(grid, target)           # SC: O(1), where n = num of rows and m = num of cols (see TC explanation below)
    if r == -1:
        return False
    return binary_search(grid[r], target)


def find_row(grid, target):
    lo = 0
    hi = len(grid) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if grid[mid][0] <= target <= grid[mid][-1]:
            return mid
        elif target < grid[mid][0]:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def binary_search(nums, target):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if target > nums[mid]:
            lo = mid + 1
        elif target < nums[mid]:
            hi = mid - 1
        else:
            return True

    return False


# Searching for the target row takes log(n) time. Likewise, searching for the target column takes log(m). The time complexity is O(log(n) + log(m)). From log rules we know that log(n) + log(m) = log(n * m), therefore the time complexity of this algorithm is O(log(n * m)) :D