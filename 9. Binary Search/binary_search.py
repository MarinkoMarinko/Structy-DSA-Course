def binary_search(numbers, target):      # TC: O(logn)
    lo = 0                               # SC: O(1), where n = len(numbers)
    hi = len(numbers) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if target < numbers[mid]:
            hi = mid - 1
        elif target > numbers[mid]:
            lo = mid + 1
        else:
            return mid

    return -1