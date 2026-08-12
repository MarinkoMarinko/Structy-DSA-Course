def has_subarray_sum(numbers, target_sum):    # TC: O(n)
    total = 0                                 # SC: O(n), where n = len(numbers)
    prefix_sum = [ 0 ]
    for num in numbers:
        total += num
        prefix_sum.append(total)

    seen = set()
    for num in prefix_sum:
        complement = num - target_sum
        if complement in seen:
            return True
        seen.add(num)

    return False