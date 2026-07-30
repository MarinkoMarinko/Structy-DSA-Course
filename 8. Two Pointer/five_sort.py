def five_sort(nums):      # TC: O(n)
    i = 0                 # SC: O(1), where n = len(nums)
    j = len(nums) - 1
    while i < j:
        if nums[j] == 5:
            j -= 1
        elif nums[i] != 5:
            i += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]

    return nums