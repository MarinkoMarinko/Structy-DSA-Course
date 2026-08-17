def pair_sum(numbers, target_sum):     # TC: O(n)
    seen = {}                          # SC: O(n), where n = len(numbers)

    for i, num in enumerate(numbers):
        complement = target_sum - num

        if complement in seen:
            return (seen[complement], i)
        
        seen[num] = i