from collections import deque

def merge_sort(nums):        # TC: O(n * logn)
    if len(nums) <= 1:       # SC: O(n), where n = len(nums)
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)


def merge(arr_1, arr_2):
    arr_1 = deque(arr_1)
    arr_2 = deque(arr_2)
    merged = []

    while arr_1 and arr_2:
        if arr_1[0] < arr_2[0]:
            merged.append(arr_1.popleft())
        else:
            merged.append(arr_2.popleft())

    merged += arr_1
    merged += arr_2
    return merged