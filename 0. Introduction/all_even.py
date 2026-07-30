def all_even(nums):        # TC: O(n)
  for num in nums:         # SC: O(1), where n = len(nums)
    if num % 2 != 0:
      return False

  return True